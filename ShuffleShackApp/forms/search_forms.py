from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms.validators import InputRequired, NumberRange
import datetime


class SearchForm(FlaskForm):
    today = datetime.date.today()
    check_in = DateField('Check In', validators=[InputRequired(message='Please enter a check in date.')],
                        render_kw={"placeholder": "Check In"}, default=today)
    check_out = DateField('Check Out', validators=[InputRequired(message='Please enter a check out date.')],
                        render_kw={"placeholder": "Check Out"}, default=today + datetime.timedelta(days=2))
    city = StringField('City', validators=[InputRequired(message='Please enter a city.')], render_kw={
                        "placeholder": "Start typing...",
                        "oninvalid": "this.setCustomValidity('Please enter a city.')",
                        "oninput": "this.setCustomValidity('')",
                        "required": True}, default='')
    guests = IntegerField('Guests', validators=[InputRequired(message='Please enter the number of guests.'),
                        NumberRange(min=1, max=12, message='Number of guests must be between 1 and 12.')],
                        render_kw={"placeholder": "Guests", "min": 1, "max": 12}, default=2)
    submit = SubmitField('Go', render_kw={"id": "submit_search"})
