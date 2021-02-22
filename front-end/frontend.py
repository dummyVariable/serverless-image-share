from app import create_app
from config import Config,TestConfig

app = create_app('prod')

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
    

app.run(port=8080)