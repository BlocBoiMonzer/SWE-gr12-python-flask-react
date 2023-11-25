import os
import tempfile
import pytest
from flaskserver import create_app
from flaskserver.models import User, Tour, Booking
from flaskserver import db

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

def test_login(client):
    response = client.post('/login', data=dict(
        username='testuser',
        password='testpassword'
    ), follow_redirects=True)
    assert b'Du har blitt logget inn!' in response.data

def test_logout(client):
    response = client.get('/index', follow_redirects=True)
    assert b'Du har blitt logget ut' in response.data

def test_show_tours(client):
    response = client.get('/tours')
    assert 'Vennligst logg inn for å se reiser.'.encode('utf-8') in response.data

def test_create_tour(client):
    response = client.post('/create_tour', data=dict(
        name='Test Tour',
        description='This is a test tour',
        price='100',
        start_date='2023-01-01',
        end_date='2023-01-07',
        image=(tempfile.NamedTemporaryFile(suffix=".png"), 'test.png')
    ), follow_redirects=True)
    assert b'Turen har blitt opprettet' in response.data

def test_book_tour(client):
    response = client.post('/book-tour/1', follow_redirects=True)
    assert 'Vennligst logg inn for å booke reiser.'.encode('utf-8') in response.data

def test_user_bookings(client):
    response = client.get('/my-bookings')
    assert 'Vennligst logg inn for å se dine bookinger.'.encode('utf-8') in response.data