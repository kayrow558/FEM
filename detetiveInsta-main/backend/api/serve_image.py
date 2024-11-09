from flask import Blueprint, send_from_directory, jsonify
import os

serve_image_blueprint = Blueprint('serve_image', __name__)

@serve_image_blueprint.route('/api/profile_images/<username>/<follower_username>/profile.jpg', methods=['GET'])
def serve_profile_image(username, follower_username):
    image_path = f"profile_images/{username}/{follower_username}/profile.jpg"
    if os.path.exists(image_path):
        return send_from_directory(f"profile_images/{username}/{follower_username}", 'profile.jpg')
    return jsonify({"error": "Image not found"}), 404
