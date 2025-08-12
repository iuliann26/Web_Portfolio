from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_wtf.csrf import CSRFProtect

# Inițializăm extensiile, dar nu le legăm încă de aplicație
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    csrf = CSRFProtect(app)

    # Inițializăm extensiile cu aplicația
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # Importuri după ce app & db sunt complet configurate
    from app.models import User
    from app.routes import main
    app.register_blueprint(main)

    # Înregistrăm funcția pentru încărcarea utilizatorului
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
