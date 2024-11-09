import os
import time
from flask import Blueprint, request, jsonify
import instaloader
from config.proxies import load_proxies
from utils.helpers import create_directory
from config.accounts import load_accounts
from utils.instaloader_wrapper import create_instaloader

download_blueprint = Blueprint('download', __name__)

def image_exists(username):
    image_path = f"profile_images/{username}/{username}.jpg"
    return os.path.exists(image_path)

@download_blueprint.route('/api/download', methods=['POST'])
def download_profile_pictures():
    data = request.get_json()
    target_username = data.get('username')
    max_followers = data.get('max_followers', 4) 
    if not target_username:
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

        main_directory = f"profile_images/{target_username}"
        create_directory(main_directory)

        profile = instaloader.Profile.from_username(L.context, target_username)
        followers = profile.get_followers()
        followers_data = []
        profileName = profile.full_name
        print(f"O Nome do perfil de {target_username} é {profileName}")
        time.sleep(1)

        for index, follower in enumerate(followers):
            if index >= max_followers:
                break

            if image_exists(follower.username):
                print(f"Imagem de {follower.username} já existe. Pulando download.")
            else:
                follower_dir = f"{main_directory}/{follower.username}"
                create_directory(follower_dir)
                L.dirname_pattern = follower_dir
                L.download_profilepic(follower)
                time.sleep(30)  # Atraso configurável para evitar limite de taxa
                print(f'Download de {follower.username} concluído, aguardando 30s para o próximo')

            followers_data.append({
                "username": follower.username,
                "profile_image": f"{follower_dir}/{follower.username}.jpg"
            })

        return jsonify({
            "message": "Imagens baixadas com sucesso!",
            "username": target_username,
            "followers": followers_data
        })

    except instaloader.exceptions.LoginRequiredException:
        return jsonify({"error": "Falha no login. Verifique as credenciais."}), 500
    except Exception as e:
        return jsonify({"error": f"Erro inesperado: {str(e)}"}), 500
