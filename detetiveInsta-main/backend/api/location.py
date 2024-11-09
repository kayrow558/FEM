from flask import Blueprint, jsonify
from getLocation import getLocation

location_blueprint = Blueprint('location', __name__)

@location_blueprint.route('/api/location', methods=['GET'])
def user_location():
    return jsonify(getLocation()), 200
