# app/__init__.py
"""Inițializează aplicația Flask și extensiile sale."""


from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from .config import Config

__all__ = ["Config"]
# Inițializăm extensiile (fără să le atașăm încă la aplicație)
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app(config_class=Config):
    """Create and configure the Flask application."""
    # Creăm instanța aplicației Flask
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inițializăm extensiile cu aplicația
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Setări pentru Flask-Login
    login_manager.login_view = "main.login"  # ruta unde trimite dacă nu e logat
    login_manager.login_message_category = (
        "info"  # mesaj flash category (Bootstrap friendly)
    )

    # Import modele și blueprint-uri după ce app & db sunt configurate
    from app.models import User
    from app.routes import main

    app.register_blueprint(main)

    # Funcția care încarcă utilizatorul din sesiune
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
