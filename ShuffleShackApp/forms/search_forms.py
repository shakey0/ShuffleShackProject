from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms.validators import InputRequired
import datetime


class SearchForm(FlaskForm):
    today = datetime.date.today()
    check_in = DateField('Check In', validators=[InputRequired(message='Please enter a check in date.')], render_kw={"placeholder": "Check In"}, default=today)
    check_out = DateField('Check Out', validators=[InputRequired(message='Please enter a check out date.')], render_kw={"placeholder": "Check Out"}, default=today + datetime.timedelta(days=2))
    city = StringField('City', validators=[InputRequired(message='Please enter a city.')], render_kw={"placeholder": "City"}, default='London')
    guests = IntegerField('Guests', validators=[InputRequired(message='Please enter the number of guests.')], render_kw={"placeholder": "Guests"}, default=2)
    submit = SubmitField('Go', render_kw={"id": "submit_search"})
