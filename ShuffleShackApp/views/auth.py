from flask import Blueprint, redirect, url_for, jsonify
from ShuffleShackApp.extensions import db
from ShuffleShackApp.models.user import User
from ShuffleShackApp.forms.auth_forms import LoginForm, RegisterForm
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, logout_user
import bcrypt


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['POST'])
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
            db.session.rollback()
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


@auth.route('/login', methods=['POST'])
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


@auth.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('main.index'))
