# app/__init__.py
"""Inițializează aplicația Flask și extensiile sale."""


from flask import Flask, Response
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from prometheus_flask_exporter import PrometheusMetrics

from .config import Config

__all__ = ["Config"]
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
metrics = PrometheusMetrics.for_app_factory()


def create_app(config_class=Config):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    metrics.init_app(app)

    @app.route("/metrics")
    @csrf.exempt
    def metrics_route():
        return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

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
