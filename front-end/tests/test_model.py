
import pytest, os

from app import create_app
from app.models import db, Post, User


@pytest.fixture(scope='module')
def client():
          
    app = create_app('test')

    with app.test_client() as client:
        with app.app_context() as app:        
            app.push()
            db.create_all()
            user1 = User(username='dude', password='dude')
            user2 = User(username='lol', password='lol')
            db.session.add_all([user1,user2])
            
        yield client
    
    app.pop()
    os.remove('data.db')

def login(client, username, password):
    return client.post('/login', data=dict(username=username, password=password), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def test_for_no_of_posts_when_post(client):
    login(client, 'dude', 'dude')

    client.post('/post', data=dict(title='Test Post 2', body='Content for test'))
    client.post('/post', data=dict(title='Test Post 3', body='Content for test'))

    assert len(Post.query.all()) == 2

def test_for_posts_written_by_username(client):

    assert len(User.query.get(1).posts) == 2 

    logout(client)
    login(client, 'lol', 'lol')

    client.post('/post', data=dict(title='Test Post 4', body='Content for test'))

    assert len(Post.query.all()) == 3
    assert len(User.query.get(1).posts) == 2 
    assert len(User.query.get(2).posts) == 1 

