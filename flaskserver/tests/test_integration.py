from config import Config
import pytest
from app import create_app
from models import Booking, Tour, User
from sqlalchemy.testing import db
from models import Tour


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

def test_login(client):
    response = client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)

    assert b'Logged in!' in response.data


def test_successful_tour_creation(client):
    response = client.post('/create_tour', data={
        'name': 'Successful Tour',
        'description': 'This is a successful test tour',
        'price': '200',
        'start_date': '2022-02-01',
        'end_date': '2022-02-28'
    })

    tour = Tour.query.filter_by(name='Successful Tour').first()
    assert tour is not None