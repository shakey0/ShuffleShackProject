from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
import re


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


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(min=1, max=30)], render_kw={"placeholder": "Email OR Username", "id": "email_login"})
    password = PasswordField('Password', validators=[InputRequired(), Length(min=1, max=30)], render_kw={"placeholder": "Password", "id": "password_login"})
    submit = SubmitField('Login', render_kw={"id": "submit_login"})


class LogoutForm(FlaskForm):
    submit = SubmitField('Logout', render_kw={"id": "submit_logout"})
