from datetime import timedelta

from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from extensions import db, migrate
from models import User

def create_app(database_uri="sqlite://"):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "hadi"
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=5)

    CORS(app)

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