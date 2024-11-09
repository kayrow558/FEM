import os
import time
from flask import Blueprint, request, jsonify
import instaloader
from config.proxies import load_proxies
from utils.helpers import create_directory
from config.accounts import load_accounts
from utils.instaloader_wrapper import create_instaloader
import random

random_follower_blueprint = Blueprint('random_follower', __name__)

@random_follower_blueprint.route('/api/random_follower/<username>', methods=['GET'])
def get_random_follower(username):
    follower_path = f'./profile_images/{username}'

    followers = [f for f in os.listdir(follower_path) if os.path.isfile(os.path.join(follower_path, 'profile_pic.jpg'))]

    if not followers:
        return jsonify({"error": "Não foi achado nenhum seguidor com imagem de perfil."})
    
    random_follower = random.choice(followers)

    return jsonify({
        "username": random_follower,
        "name": f"Nome de usuário: {random_follower}",
        "image_url": f"/api/profile_images/{username}/{random_follower}/profilepic.jpg"
    })