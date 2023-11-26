from unittest.mock import patch
from models import User, Booking, Tour

def test_user_creation():
    user = User(username='testuser', email='test@example.com')
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'

def test_booking_creation():
    booking = Booking(user_id=1, tour_id=1)
    assert booking.user_id == 1
    assert booking.tour_id == 1

def test_tour_creation():
    tour = Tour(name='Test Tour', description='This is a test tour')
    assert tour.name == 'Test Tour'
    assert tour.description == 'This is a test tour'
