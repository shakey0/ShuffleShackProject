from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo, ValidationError
from ShuffleShackApp.extensions import db
from ShuffleShackApp.models.user import User
from ShuffleShackApp.models.property import Property
from ShuffleShackApp.models.room import Room
from ShuffleShackApp.models.booking import Booking
from sqlalchemy.sql.expression import func, desc


main = Blueprint('main', __name__)


def get_popular_properties():

    subquery = db.session.query(
            func.max(Property.id).label('max_id'),
            Property.city
        ) \
        .filter(func.cast(Property.review_data['average_rating'], db.Integer) >= 40) \
        .group_by(Property.city) \
        .subquery()

    lowest_price_room_subquery = db.session.query(
            Room.property_id,
            func.min(Room.price).label('min_price')
        ) \
        .group_by(Room.property_id) \
        .subquery()

    properties = db.session.query(
            Property,
            Room
        ) \
        .join(subquery, Property.id == subquery.c.max_id) \
        .join(Room, Property.id == Room.property_id) \
        .join(lowest_price_room_subquery, (Room.property_id == lowest_price_room_subquery.c.property_id) & (Room.price == lowest_price_room_subquery.c.min_price)) \
        .order_by(func.random()) \
        .limit(30) \
        .all()

    return properties


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=6, max=30)], render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=30)], render_kw={"placeholder": "Password"})
    submit = SubmitField('Login')


@main.route('/', methods=['GET', 'POST'])
def index():

    login_form = LoginForm()

    properties_and_rooms = get_popular_properties()

    return render_template('index.html', properties_and_rooms=properties_and_rooms)
