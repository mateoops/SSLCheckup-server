from flask import Blueprint, jsonify

ssl_bp = Blueprint('ssl', __name__)

@ssl_bp.route('/ssl', methods=['GET'])
def get_ssl_configurations():
    # Logic to fetch SSL configurations from the database
    ssl_configs = [
        {
            'id': 1,
            'host': 'example.com',
            'address': '192.168.0.1',
            'description': 'Sample SSL configuration',
            'port': 443
        },
        # Add more SSL configurations as needed
    ]

    return jsonify(ssl_configs)
