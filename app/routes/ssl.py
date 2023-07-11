from flask import Blueprint, jsonify, request
from app.models.ssl_configuration import SSLConfiguration

ssl_bp = Blueprint('ssl', __name__)

@ssl_bp.route('/ssl', methods=['GET'])
def get_ssl_configurations():
    ssl_configs = SSLConfiguration.get_all()

    return jsonify(ssl_configs)

@ssl_bp.route('/ssl', methods=['POST'])
def set_ssl_configuration():

    data = request.get_json()

    response = SSLConfiguration.save(data['host'], data['address'], data['port'], data['description'])

    response = {'message': 'Data processed successfully'}
    return jsonify(response), 200
