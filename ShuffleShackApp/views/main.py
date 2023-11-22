from flask import Blueprint, render_template, request, session
from ShuffleShackApp.query_functions import get_popular_properties, get_search_properties
from ShuffleShackApp.forms.auth_forms import LoginForm, RegisterForm, LogoutForm
from ShuffleShackApp.forms.search_forms import SearchForm
from ShuffleShackApp.utils import format_price, first_three_characters, description_limiter, \
room_name_checker, format_beds
from flask_login import current_user
from datetime import datetime, date, timedelta


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():

    search_query = request.args

    if search_query:
        print('SEARCH QUERY FOUND')
        check_in = search_query['check_in']
        check_out = search_query['check_out']
        city = search_query['city']
        number_of_guests = int(search_query['guests'])
        session['search_query'] = [check_in, check_out, city, number_of_guests]
        
        properties_and_rooms = get_search_properties(check_in, check_out, city, number_of_guests)
        in_search = True
    else:
        print('NO SEARCH QUERY FOUND')
        properties_and_rooms = get_popular_properties()
        in_search = False

    if 'search_query' in session:
        search_query_data = session['search_query']
        previous_check_in = datetime.strptime(search_query_data[0], '%Y-%m-%d').date()
        previous_check_out = datetime.strptime(search_query_data[1], '%Y-%m-%d').date()
        previous_city = search_query_data[2]
        previous_guests = search_query_data[3]
        search_form = SearchForm(check_in=previous_check_in, check_out=previous_check_out, city=previous_city, guests=previous_guests)
        min_check_out_date = previous_check_in + timedelta(days=1)
    else:
        search_form = SearchForm()
        min_check_out_date = date.today() + timedelta(days=1)

    latest_check_in = date.today() + timedelta(days=299)
    search_form.check_in.render_kw = {'min': date.today().strftime('%Y-%m-%d'), 'max': latest_check_in.strftime('%Y-%m-%d')}
    
    latest_check_out = date.today() + timedelta(days=300)
    search_form.check_out.render_kw = {'min': min_check_out_date.strftime('%Y-%m-%d'), 'max': latest_check_out.strftime('%Y-%m-%d')}

    login_form = LoginForm()

    register_form = RegisterForm()

    logout_form = LogoutForm()

    return render_template('index.html', search_form=search_form, login_form=login_form,
                            register_form=register_form, logout_form=logout_form, user=current_user,
                            properties_and_rooms=properties_and_rooms,
                            in_search=in_search, format_price=format_price,
                            first_three_characters=first_three_characters,
                            description_limiter=description_limiter,
                            room_name_checker=room_name_checker, format_beds=format_beds)
