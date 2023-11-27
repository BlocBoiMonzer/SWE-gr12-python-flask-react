from datetime import timedelta

from flask import Flask
from flask_cors import CORS
from config import Config
from flask_login import LoginManager
from extensions import db, migrate
from models import User

def create_app(database_uri="sqlite://"):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "main.login" 

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    from routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app