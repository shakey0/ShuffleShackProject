from flask import Flask
from ShuffleShackApp.extensions import db
from ShuffleShackApp.config import DevelopmentConfig
from seed_data import init_users, init_properties, init_rooms, init_bookings

def seed_dev_database():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
        init_users(db)
        init_properties(db)
        init_rooms(db)
        init_bookings(db)
        db.session.remove()

seed_dev_database()
