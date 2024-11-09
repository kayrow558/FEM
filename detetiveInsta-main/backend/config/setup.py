import os
from dotenv import load_dotenv
from api.download import download_blueprint
from api.followers import followers_blueprint
from api.location import location_blueprint
from api.serve_image import serve_image_blueprint
from api.profile_api import profile_api_blueprint
from api.random_follower import random_follower_blueprint

def initialize_app(app):
    load_dotenv()
    app.register_blueprint(followers_blueprint)
    app.register_blueprint(location_blueprint)
    app.register_blueprint(serve_image_blueprint)
    app.register_blueprint(download_blueprint)
    app.register_blueprint(profile_api_blueprint)
    app.register_blueprint(random_follower_blueprint)
