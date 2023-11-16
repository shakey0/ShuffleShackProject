from flask import Blueprint
from ShuffleShackApp.extensions import db
from ShuffleShackApp.models.user import User
from flask import render_template
import random
import string

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # { }
    random_username = ''.join(random.choices(string.ascii_lowercase, k=10))
    random_email = '{}@example.com'.format(random_username)

    new_user = User(username=random_username, email=random_email)

    db.session.add(new_user)
    db.session.commit()

    last_user = User.query.order_by(User.id.desc()).first()

    return '<h1>Hello world!</h1><br>Last added user: {} with email {}'.format(last_user.username, last_user.email)
