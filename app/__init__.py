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
    from app.routes.main_routes import main as main_blueprint
    from app.routes.exercise_routes import exercise as exercise_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(exercise_blueprint)
    return app
