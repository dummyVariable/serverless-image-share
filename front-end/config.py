import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASEDIR}/data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'secret'
    BOOTSTRAP_USE_MINIFIED = True

class TestConfig(Config):
    WTF_CSRF_ENABLED = False


option = {
    'prod' : Config(),
    'test' : TestConfig()
}