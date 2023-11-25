import pytest, os
from flask import Flask
from app import create_app
from sqlalchemy.testing import db
from models import Booking, Tour, User
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


@pytest.fixture
def client():

    app = create_app()

    with app.test_client() as test_client:

        with app.app_context():
            db.create_all()

            yield test_client

            db.session.remove()
            db.drop_all()


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

def test_user_model(client):
    user = User(firstname='John', lastname='Doe', phonenumber='123456789', address='123 Main St', email='john.doe@example.com', username='johndoe', password='password123')
    db.session.add(user)
    db.session.commit()
    assert User.query.filter_by(username='johndoe').first() is not None


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

def test_login_failure(client):
    response = client.post('/login', data={
    'username': 'wronguser',
    'password': 'wrongpassword'
}, follow_redirects=True)

    assert b'Invalid credentials' in response.data

def test_protected_route(client):
    response = client.get('/protected_route', follow_redirects=True)
    assert b'Please log in to access this page.' in response.data

def test_create_tour(client):
    response = client.post('/create_tour', data={
        'name': 'Test Tour',
        'description': 'This is a test tour',
        'price': '100',
        'start_date': '2022-01-01',
        'end_date': '2022-01-31'
    })

    tour = Tour.query.filter_by(name='Test Tour').first()
    assert tour is not None

def test_successful_tour_creation(client):
    response = client.post('/create_tour', data={
    'name': 'Test Tour',
    'description': 'This is a test tour',
    'price': '100',
    'start_date': '2022-01-01',
    'end_date': '2022-01-31'
})

    tour = Tour.query.filter_by(name='Test Tour').first()
    assert tour is not None

def test_unsuccessful_tour_creation(client):
    response = client.post('/create_tour', data={
        'name': '',
        'description': '',
        'price': '',
        'start_date': '',
        'end_date': ''
    })

    assert b'Invalid tour data' in response.data

def test_successful_booking(client):
    tour = Tour.query.filter_by(name='Test Tour').first()
    response = client.post(f'/book-tour/{tour.id}', data={})

    booking = Booking.query.filter_by(tour_id=tour.id).first()
    assert booking is not None

def test_unsuccessful_booking(client):
    response = client.post('/book-tour/999', data={})

    assert b'Tour does not exist' in response.data

def test_user_authentication(client):
    response = client.get('/create_tour', follow_redirects=True)

    assert b'Please log in to access this page.' in response.data

def test_user_authorization(client):
    tour = Tour.query.filter_by(name='Test Tour').first()
    response = client.post(f'/book-tour/{tour.id}', data={}, follow_redirects=True)

    assert b'You cannot book your own tour.' in response.data

def test_viewing_bookings(client):
    response = client.get('/my-bookings', follow_redirects=True)

    assert b'Your bookings' in response.data