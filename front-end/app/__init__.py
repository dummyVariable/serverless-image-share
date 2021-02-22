from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

from config import option

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(env):
    
    app = Flask(__name__)
    app.config.from_object(option[env])

    db.init_app(app)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    login_manager.init_app(app)
    bootstrap.init_app(app)


    return app