import pytest
from flaskserver.server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_members_route(client):
    rv = client.get('/members')
    assert rv.status_code == 200
    assert rv.get_json() == {"members": ["Member1", "Member2", "Member3", "Member4", "Ali"]}


class User:
    def __init__(self, username):
        self.username = username
        self.selected_trip = None
        self.selected_payment_method = None


def choose_trip(user, trip_id):
    user.selected_trip = trip_id


def choose_payment_method(user, payment_method):
    user.selected_payment_method = payment_method


def test_user_initialization():
    username = "Hadi"
    user = User(username)
    assert user.username == username
    assert user.selected_trip is None
    assert user.selected_payment_method is None


def test_choose_trip():
    user = User("Hadi")
    trip_id = 12
    choose_trip(user, trip_id)
    assert user.selected_trip == trip_id


def test_choose_payment_method():
    user = User("Hadi")
    payment_method = "vipps"
    choose_payment_method(user, payment_method)
    assert user.selected_payment_method == payment_method