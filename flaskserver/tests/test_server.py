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