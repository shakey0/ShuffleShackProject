from flask import Blueprint, render_template, request
from ShuffleShackApp.big_queries import get_popular_properties, get_search_properties
from ShuffleShackApp.forms.auth_forms import LoginForm, RegisterForm, LogoutForm
from ShuffleShackApp.forms.search_forms import SearchForm
from ShuffleShackApp.utils import format_price, first_three_characters, description_limiter, divide_capacity_for_bed_type
from flask_login import current_user


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():

    search_query = request.args
    print(search_query)

    if search_query:
        print('SEARCH QUERY FOUND')
        check_in = search_query['check_in']
        check_out = search_query['check_out']
        city = search_query['city']
        number_of_guests = int(search_query['guests'])
        
        properties_and_rooms = get_search_properties(check_in, check_out, city, number_of_guests)
        in_search = True
    else:
        print('NO SEARCH QUERY FOUND')
        properties_and_rooms = get_popular_properties()
        in_search = False
    
    search_form = SearchForm()

    login_form = LoginForm()

    register_form = RegisterForm()

    logout_form = LogoutForm()

    return render_template('index.html', search_form=search_form, login_form=login_form, register_form=register_form,
                            logout_form=logout_form, user=current_user, properties_and_rooms=properties_and_rooms,
                            in_search=in_search, format_price=format_price, first_three_characters=first_three_characters,
                            description_limiter=description_limiter, divide_capacity_for_bed_type=divide_capacity_for_bed_type)
