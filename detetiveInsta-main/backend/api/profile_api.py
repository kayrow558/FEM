from flask import Blueprint, request, jsonify
import instaloader
import os
from utils.helpers import create_directory
from config.accounts import load_accounts
from config.proxies import load_proxies
from utils.instaloader_wrapper import create_instaloader

profile_api_blueprint = Blueprint('profile_api', __name__)

def image_exists(username):
    image_path = f"profile_images/{username}/{username}.jpg"
    return os.path.exists(image_path)

@profile_api_blueprint.route('/api/download/profile', methods=['POST'])
def download_single_profile_picture():
    data = request.get_json()
    username = data.get('username')
    if not username:
        return jsonify({"error": "Nome de usuário não fornecido."}), 400

    accounts = load_accounts()
    if not accounts:
        return jsonify({"error": "Nenhuma conta disponível"}), 500

    try:
        proxies = load_proxies()
        selected_account = accounts[0]
        selected_proxy = proxies[0] if proxies else None
        L = create_instaloader(proxy=selected_proxy)
        L.login(selected_account['username'], selected_account['password'])
        print(f"Login feito na conta {selected_account}, utilizando a proxy {selected_proxy}")

        main_directory = f"profile_images/{username}"
        create_directory(main_directory)

        if image_exists(username):
            print(f"Imagem de {username} já existe. Pulando download.")
            return jsonify({"message": f"A imagem de perfil de {username} já existe."})

        profile = instaloader.Profile.from_username(L.context, username)
        L.dirname_pattern = main_directory
        L.download_profilepic(profile)
        print(f"Download da imagem de perfil de {username} concluído")

        return jsonify({"message": "Imagem de perfil baixada com sucesso!", "username": username})

    except instaloader.exceptions.LoginRequiredException:
        return jsonify({"error": "Falha no login. Verifique as credenciais."}), 500
    except instaloader.exceptions.ProfileNotExistsException:
        return jsonify({"error": "Perfil não encontrado."}), 404
    except Exception as e:
        return jsonify({"error": f"Erro inesperado: {str(e)}"}), 500