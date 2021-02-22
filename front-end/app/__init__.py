from flask import Flask
from flask_bootstrap import Bootstrap

from config import option

bootstrap = Bootstrap()

def create_app(env):
    
    app = Flask(__name__)
    app.config.from_object(option[env])

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    bootstrap.init_app(app)


    return app