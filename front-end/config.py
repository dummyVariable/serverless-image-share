import os


class Config:

    SECRET_KEY = 'secret'
    BOOTSTRAP_USE_MINIFIED = True

class TestConfig(Config):
    WTF_CSRF_ENABLED = False


option = {
    'prod' : Config(),
    'test' : TestConfig()
}