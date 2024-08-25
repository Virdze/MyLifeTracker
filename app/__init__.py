from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine
from config import DevelopmentConfig

# Initialize MongoDB
db = MongoEngine()

def create_app(config_name='development'):
    app = Flask(__name__)
    CORS(app)
    # Load configuration
    app.config.from_object({
        'development' : DevelopmentConfig
    }[config_name])

    # Initialize MongoDB
    db.init_app(app)

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
