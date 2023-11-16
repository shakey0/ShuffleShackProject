import pytest
from flask import Flask
from ShuffleShackApp import db
from ShuffleShackApp.config import TestingConfig
from ShuffleShackApp.models.test_table import RunTable

@pytest.fixture(scope='module')
def test_app():
    app = Flask(__name__)
    app.config.from_object(TestingConfig)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture(scope='module')
def test_client(test_app):
    with test_app.test_client() as client:
        yield client

@pytest.fixture(scope='function')
def seed_database(test_app):
    with test_app.app_context():
        db.session.add(RunTable(name='first_record'))
        db.session.commit()
