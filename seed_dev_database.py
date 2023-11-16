from flask import Flask
from ShuffleShackApp.extensions import db
from ShuffleShackApp.config import DevelopmentConfig
from seed_data import init_user, init_property, init_room

def seed_dev_database():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
        init_user(db)
        init_property(db)
        init_room(db)
        db.session.remove()

seed_dev_database()
