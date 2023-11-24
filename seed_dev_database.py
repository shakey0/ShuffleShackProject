#  This file is used to seed the database with data for development purposes.

from flask import Flask
from ShuffleShackApp.extensions import db
from ShuffleShackApp.config import DevelopmentConfig
from seed_data import init_users, init_properties, init_rooms, init_bookings
from seed_data_random import init_random_data

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

seed_with_default_data = input('Seed database with default data? (y/n): ')

if seed_with_default_data == 'y':
    seed_dev_database()
    print('Database seeded with default data.')

seed_with_random_data = input('Seed database with random data? (y/n): ')

if seed_with_random_data == 'y':
    number_of_users = input('How many users? ')
    number_of_properties = input('How many properties? ')
    number_of_rooms = input('How many rooms? ')
    # number_of_bookings = input('How many bookings? ')
    init_random_data(db, seed_with_default_data, int(number_of_users), int(number_of_properties), int(number_of_rooms))
