from app import create_app
from config import Config,TestConfig

app = create_app('prod')

app.run(port=8080)