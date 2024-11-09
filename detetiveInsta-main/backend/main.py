from flask import Flask
from flask_cors import CORS
from config.setup import initialize_app
from utils.helpers import rename_profile_pics


app = Flask(__name__)
CORS(app)
initialize_app(app)

rename_profile_pics()

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=False)
