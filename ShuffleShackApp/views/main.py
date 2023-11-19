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
from flask_login import login_user, logout_user, current_user, login_required
import re
import bcrypt


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


def format_price(price):
    return f'{price/100:.2f}'


class PasswordComplexityValidator(object):
    def __init__(self, message=None):
        if not message:
            message = u'Password must include at least one lowercase letter, one uppercase letter, one digit, and one special character.'
        self.message = message

    def __call__(self, form, field):
        if not re.search("[a-z]", field.data):
            raise ValidationError(self.message)
        elif not re.search("[A-Z]", field.data):
            raise ValidationError(self.message)
        elif not re.search("[0-9]", field.data):
            raise ValidationError(self.message)
        elif not re.search("[!@#$%^&*(),.?\":{}|<>]", field.data):
            raise ValidationError(self.message)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=6, max=30)], render_kw={"placeholder": "Email OR Username", "id": "email_login"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=30)], render_kw={"placeholder": "Password", "id": "password_login"})
    submit = SubmitField('Login', render_kw={"id": "submit_login"})


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "First Name"})
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=2, max=30)], render_kw={"placeholder": "Last Name"})
    user_name = StringField('Username', validators=[InputRequired(), Length(min=6, max=30)], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)], render_kw={"placeholder": "Email"})
    phone_number = StringField('Phone Number', validators=[InputRequired(), Length(min=10, max=20)], render_kw={"placeholder": "Phone Number"})
    date_of_birth = DateField('Date of Birth', validators=[InputRequired()], render_kw={"placeholder": "Date of Birth"})
    nationality = StringField('Nationality', validators=[InputRequired()], render_kw={"placeholder": "Nationality"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=30), PasswordComplexityValidator()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), Length(min=8, max=30), EqualTo('password', message='Passwords must match')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Register')


@main.route('/', methods=['GET'])
def index():

    login_form = LoginForm()

    register_form = RegisterForm()

    properties_and_rooms = get_popular_properties()

    return render_template('index.html', login_form=login_form, register_form=register_form, properties_and_rooms=properties_and_rooms, format_price=format_price)


@main.route('/login', methods=['POST'])
def login():

    login_form = LoginForm()

    # if login_form.validate_on_submit():

    #     username = login_form.username.data
    #     password = login_form.password.data

    #     user = User.query.filter_by(email=username).first() or User.query.filter_by(user_name=username).first()

    #     if user and user.password == password:
    #         return redirect(url_for('main.index'))
    #     else:
    #         flash('Invalid username or password', 'danger')
    #         return redirect(url_for('main.index'))

    # else:
    #     flash('Invalid username or password', 'danger')
    #     return redirect(url_for('main.index'))

    print('WE GOT HERE LOGIN')

    return redirect(url_for('main.index'))


@main.route('/register', methods=['POST'])
def register():
    

    register_form = RegisterForm()

    if register_form.validate_on_submit():
        print('WE GOT HERE RESISTER')
    else:
        print('SOMETHING WENT WRONG')
        for fieldName, errorMessages in register_form.errors.items():
            for err in errorMessages:
                print(f"Error in {fieldName}: {err}")


    return redirect(url_for('main.index'))