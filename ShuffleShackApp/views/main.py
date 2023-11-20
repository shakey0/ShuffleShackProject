from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo, ValidationError
from ShuffleShackApp.extensions import db
from ShuffleShackApp.models.user import User
from ShuffleShackApp.models.property import Property
from ShuffleShackApp.models.room import Room
from ShuffleShackApp.models.booking import Booking
from sqlalchemy.sql.expression import func, desc
from sqlalchemy.exc import IntegrityError
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


def first_three_characters(user_name):
    return user_name[:3]


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
    email = StringField('Email', validators=[InputRequired(), Length(min=1, max=30)], render_kw={"placeholder": "Email OR Username", "id": "email_login"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=30)], render_kw={"placeholder": "Password", "id": "password_login"})
    submit = SubmitField('Login', render_kw={"id": "submit_login"})


class RegisterForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(message='Please enter your first name.'), Length(min=2, max=30, message='First name must be between 2 and 30 characters long')], render_kw={"placeholder": "First Name"})
    last_name = StringField('Last Name', validators=[InputRequired(message='Please enter your last name.'), Length(min=2, max=30, message='Last name must be between 2 and 30 characters long')], render_kw={"placeholder": "Last Name"})
    user_name = StringField('Username', validators=[InputRequired(message='Please choose a username.'), Length(min=6, max=30, message='Username must be between 6 and 30 characters long')], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[InputRequired(message='Please enter your email.'), Email(message='Invalid email address'), Length(max=50, message='Email must be less than 50 characters long')], render_kw={"placeholder": "Email"})
    phone_number = StringField('Phone Number', validators=[InputRequired(message='Please enter your phone number.'), Length(min=10, max=20, message='Phone number must be between 10 and 20 characters long')], render_kw={"placeholder": "Phone Number"})
    date_of_birth = DateField('Date of Birth', validators=[InputRequired(message='Please enter your date of birth.')], render_kw={"placeholder": "Date of Birth"})
    nationality = StringField('Nationality', validators=[InputRequired(message='Please enter your nationality.')], render_kw={"placeholder": "Nationality"})
    password = PasswordField('Password', validators=[InputRequired(message='Please enter a password.'), Length(min=8, max=30), PasswordComplexityValidator()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(message='Please confirm your password.'), Length(min=8, max=30), EqualTo('password', message='Passwords must match')], render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField('Register', render_kw={"id": "submit_register"})


class LogoutForm(FlaskForm):
    submit = SubmitField('Logout', render_kw={"id": "submit_logout"})


@main.route('/', methods=['GET'])
def index():

    login_form = LoginForm()

    register_form = RegisterForm()

    logout_form = LogoutForm()

    properties_and_rooms = get_popular_properties()

    return render_template('index.html', login_form=login_form, register_form=register_form,
                            logout_form=logout_form, user=current_user, properties_and_rooms=properties_and_rooms,
                            format_price=format_price, first_three_characters=first_three_characters)


@main.route('/login', methods=['POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        print('WE GOT HERE - LOGIN')
        
        credential = login_form.email.data
        user = User.query.filter((User.email == credential) | (User.user_name == credential)).first()

        if user:
            print('USER FOUND')
            if bcrypt.checkpw(login_form.password.data.encode('utf-8'), user.password):
                print('PASSWORD MATCHED')
                login_user(user)
                return jsonify(success=True)
            else:
                return jsonify(success=False, error="Something didn\'t match! Please try again.")
        else:
            return jsonify(success=False, error="Something didn\'t match! Please try again.")

    elif login_form.email.data == '':
        return jsonify(success=False, error="Please enter your email or username.")

    elif login_form.password.data == '':
        return jsonify(success=False, error="Please enter your password.")

    for fieldName, errorMessages in login_form.errors.items():
        for err in errorMessages:
            print(f"Error in {fieldName}: {err}")
    return redirect(url_for('main.index'))


@main.route('/register', methods=['POST'])
def register():

    register_form = RegisterForm()

    if register_form.validate_on_submit():
        print('WE GOT HERE - RESISTER')
        hashed_password = bcrypt.hashpw(register_form.password.data.encode('utf-8'), bcrypt.gensalt())
        user = User(first_name=register_form.first_name.data, last_name=register_form.last_name.data,
                    user_name=register_form.user_name.data, email=register_form.email.data,
                    phone_number=register_form.phone_number.data, password=hashed_password,
                    d_o_b=register_form.date_of_birth.data, nationality=register_form.nationality.data,
                    t_bookings=0, no_shows=0, guest_complaints=0, host_complaints=0, is_admin=False)
        try:
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return jsonify(success=True)
        except IntegrityError as e:
            db.session.rollback()  # Rollback the transaction to keep the session clean
            if 'user_name' in str(e.orig):
                return jsonify(success=False, error="Username already exists.")
            elif 'email' in str(e.orig):
                return jsonify(success=False, error="An account with this email already exists.")
            else:
                return jsonify(success=False, error='An error occurred. Please try again.')
        
    else:
        print('SOMETHING WENT WRONG')
        for fieldName, errorMessages in register_form.errors.items():
            for err in errorMessages:
                print(f"Error in {fieldName}: {err}")
        return jsonify(success=False, error='An error occurred. Please try again.', form_errors=register_form.errors)


@main.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))
