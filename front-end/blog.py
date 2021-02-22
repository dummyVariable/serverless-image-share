from flask_migrate import Migrate

from app import create_app, db
from app.models import User, Post
from config import Config,TestConfig

app = create_app('prod')
Migrate(app, db)

@app.shell_context_processor
def make_shell():
    return dict(db=db, User=User, Post=Post)

@app.cli.command('create-db')
def create_db():
    db.create_all()
