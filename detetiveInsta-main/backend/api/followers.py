from flask import Blueprint, jsonify
import os

import instaloader
from utils.instaloader_wrapper import create_instaloader

followers_blueprint = Blueprint('followers', __name__)

@followers_blueprint.route('/api/followers/<username>', methods=['GET'])
def get_followers(username):
    L = create_instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    followers = profile.get_followers()
    follower_list = [
        {"username": follower.username, "name": follower.full_name}
        for follower in followers
        if os.path.exists(f"profile_images/{username}/{follower.username}/profile.jpg")
    ]
    return jsonify(follower_list[:30])
