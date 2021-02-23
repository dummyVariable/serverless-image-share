from app import create_app
from config import Config,TestConfig

from app.auth.model import is_logged

app = create_app('prod')

@app.context_processor
def check_if_logged_in():
    return dict(login=is_logged())
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
    

app.run(port=8080)