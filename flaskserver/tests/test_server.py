import pytest

from sqlalchemy.testing import db
from flaskserver.server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_register(client):
    response = client.post('/register', data={
        'firstname': 'John',
        'lastname': 'Doe',
        'phonenumber': '123456789',
        'address': '123 Main St',
        'email': 'john.doe@example.com',
        'username': 'johndoe',
        'password': 'password123'
    })

    assert b'Registration successful!' in response.data


def test_login(client):
    client.post('/register', data={
        'firstname': 'Test',
        'lastname': 'User',
        'phonenumber': '987654321',
        'address': '456 Oak St',
        'email': 'test.user@example.com',
        'username': 'testuser',
        'password': 'testpassword'
    })

    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)

    assert b'Logged in!' in response.data