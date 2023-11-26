import pytest

from flaskserver import create_app
from configparser import ConfigParser


@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_register(client):
    data = {
        "firstname": "John",
        "lastname": "Doe",
        "phonenumber": "1234567890",
        "address": "123 Street, City",
        "email": "john.doe@example.com",
        "username": "johndoe",
        "password": "password123"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 201

def test_login(client):
    # Test the login functionality
    data = {
        "username": "johndoe",
        "password": "password123"
    }
    response = client.post('/login', data=data)
    assert b'Du har blitt logget inn!' in response.data

def test_protected_route(client):
    response = client.get('/protected-route')
    assert response.status_code == 200
    assert b'Protected Route' in response.data

def test_create_tour(client):
    data = {
        "tour_name": "Test Tour",
        "description": "This is a test tour",
        "location": "Test Location",
        "price": 100
    }
    response = client.post('/create-tour', json=data)
    assert response.status_code == 201

def test_successful_tour_creation(client):
    data = {
        "tour_name": "Test Tour",
        "description": "This is a test tour",
        "location": "Test Location",
        "price": 100
    }
    response = client.post('/create-tour', json=data)
    assert response.status_code == 201
    assert b'Tour created successfully' in response.data

def test_unsuccessful_tour_creation(client):
    data = {
        "tour_name": "Test Tour",
        "description": "This is a test tour",
        "location": "Test Location"
    }
    response = client.post('/create-tour', json=data)
    assert response.status_code == 400
    assert b'Error creating tour' in response.data

def test_successful_booking(client):

    data = {
        "tour_id": 1,
        "user_id": 1,
        "booking_date": "2023-12-01"
    }
    response = client.post('/book-tour', json=data)
    assert response.status_code == 201
    assert b'Booking successful' in response.data

def test_unsuccessful_booking(client):

    data = {
        "tour_id": 1,
        "user_id": 1
    }
    response = client.post('/book-tour', json=data)
    assert response.status_code == 400
    assert b'Error booking tour' in response.data

def test_user_authentication(client):
    data = {
        "username": "johndoe",
        "password": "password123"
    }
    response = client.post('/authenticate', data=data)
    assert response.status_code == 200
    assert b'User authenticated' in response.data

def test_user_authorization(client):
    response = client.get('/admin-panel')
    assert response.status_code == 403
    assert b'Unauthorized' in response.data

def test_viewing_bookings(client):
    with client.session_transaction() as session:
        session['user'] = 'johndoe'
    response = client.get('/my-bookings')
    assert response.status_code == 200
    assert b'My Bookings' in response.data