
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
            user = User(username='dude', password='dude')
            db.session.add(user)
            
        yield client
    
    app.pop()
    os.remove('data.db')

def login(client, username, password):
    return client.post('/login', data=dict(username=username, password=password), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def test_home_without_login(client):
    resp = client.get('/')
    assert resp.status_code == 302
    assert '/login' in resp.location
    


def test_home_with_login(client):
    login(client, 'dude', 'dude')

    resp = client.get('/')
    assert resp.status_code == 200
    assert 'No posts' in str(resp.data)
    assert 'Logout' in str(resp.data)
    assert 'Login' not in str(resp.data)



def test_for_posting_post(client):
    
    resp = client.post('/post', data=dict(title='Test Post', body='Content for test'))
    assert resp.status_code == 302

def test_for_home_after_post(client):

    resp = client.get('/')
    assert resp.status_code == 200
    assert 'Test Post' in str(resp.data)
    assert 'Content for test'
    assert 1 == len(Post.query.all())
    assert 1 == len(User.query.all())

def test_for_about_me(client):
    
    resp = client.get('/about')
    assert 'dude' in str(resp.data)
    assert 'My Posts' in str(resp.data)

def test_for_cannot_login_or_register_when_already_logged_in(client):

    resp = client.get('/login')
    assert resp.status_code == 302
    assert '/login' not in resp.location

    resp = client.get('/register')
    assert resp.status_code == 302
    assert '/register' not in resp.location


def test_for_logout(client):
    
    logout(client)
    resp = client.get('/')
    assert resp.status_code == 302
    assert '/login' in resp.location

def test_for_still_logged_out(client):

    resp = client.get('/login')

    assert resp.status_code == 200
    assert 'Login' in str(resp.data)
    assert 'Register' in str(resp.data)
