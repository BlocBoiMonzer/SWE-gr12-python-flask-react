import pytest
from flask_sqlalchemy import SQLAlchemy

from flaskserver.app import create_app

db = SQLAlchemy()

@pytest.fixture
def app():
    app = create_app("sqlite:///:memory:")
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client