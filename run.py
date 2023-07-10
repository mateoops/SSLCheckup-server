from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config')


# Initialize database
db = SQLAlchemy(app)

# Import all models
#from app.models.ssl_configuration import SSLConfiguration

# Import routes
from app.routes.ssl import ssl_bp

# Register blueprints
app.register_blueprint(ssl_bp)

if __name__ == '__main__':
    app.run(debug=True,port=8000)