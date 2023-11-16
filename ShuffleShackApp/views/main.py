from flask import Blueprint
from ShuffleShackApp.extensions import db
from ShuffleShackApp.models.user import User
from ShuffleShackApp.models.property import Property
from ShuffleShackApp.models.room import Room
from flask import render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():

    user = User.query.filter_by(id=1).first()
    print(f'user: {user}')
    property = Property.query.filter_by(id=1).first()
    print(property)
    room = Room.query.filter_by(id=1).first()
    print(room)

    return '<h1>Hello world!</h1><br>User: {user}<br>Property: {property}<br>Room: {room}'.format(user=user.user_name, property=property.name, room=room.name)
