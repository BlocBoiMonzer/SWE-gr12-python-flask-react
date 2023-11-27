import pytest
from app import create_app, db
from conftest import Config

@pytest.fixture
def app():
    app = create_app(config_class=Config)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_register_success(client):
    data = {
        "firstname": "John",
        "lastname": "Doe",
        "phonenumber": "123456789",
        "address": "123 Main St",
        "email": "john.doe@example.com",
        "username": "johndoe",
        "password": "password123"
    }
    response = client.post('/register', json=data)

    assert response.status_code == 201
    assert b"Registration successful!" in response.data

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_register_existing_username(client):
    data = {
        "firstname": "Alice",
        "lastname": "Smith",
        "phonenumber": "123456789",
        "address": "123 Main St",
        "email": "alice.smith@example.com",
        "username": "existinguser",
        "password": "password123"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 400
    assert b"Username already exists" in response.data

def test_register_new_user(client):
    data = {
        "firstname": "Bob",
        "lastname": "Johnson",
        "phonenumber": "987654321",
        "address": "456 Elm St",
        "email": "bob.johnson@example.com",
        "username": "newuser",
        "password": "password456"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 201
    assert b"Registration successful!" in response.data


def test_user_page(client):
    with client.session_transaction() as session:
        session['user'] = 'johndoe'
    response = client.get('/user')
    assert response.status_code == 200

def test_update_user(client):
    with client.session_transaction() as session:
        session['user'] = 'johndoe'
    data = {
        "firstname": "UpdatedFirstName",
        "lastname": "UpdatedLastName",
        "email": "updatedemail@example.com"
    }
    response = client.post('/user/update', data=data)
    assert response.status_code == 302

def test_login(client):
    data = {
        "username": "johndoe",
        "password": "password123"
    }
    response = client.post('/login', json=data)
    assert response.status_code == 200

def test_logout(client):
    response = client.get('/index')
    assert response.status_code == 302

def test_show_tours(client):
    with client.session_transaction() as session:
        session['user'] = 'johndoe'
    response = client.get('/tours')
    assert response.status_code == 200

def test_create_tour(client):
    with client.session_transaction() as session:
        session['user'] = 'johndoe'
    data = {
        "name": "New Tour",
        "description": "Exciting tour description",
        "price": "100",
        "start_date": "2023-01-01",
        "end_date": "2023-01-07"
    }
    response = client.post('/create_tour', data=data)
    assert response.status_code == 302

def test_book_tour(client):
    with client.session_transaction() as session:
        session['user'] = 'johndoe'
    tour_id = 1
    response = client.get(f'/book-tour/{tour_id}')
    assert response.status_code == 200

def test_user_bookings(client):
    with client.session_transaction() as session:
        session['user'] = 'johndoe'
    response = client.get('/my-bookings')
    assert response.status_code == 200