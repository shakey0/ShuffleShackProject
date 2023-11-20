from flask import Blueprint, render_template
from ShuffleShackApp.big_queries import get_popular_properties
from ShuffleShackApp.forms.auth_forms import LoginForm, RegisterForm, LogoutForm
from ShuffleShackApp.forms.search_forms import SearchForm
from ShuffleShackApp.utils import format_price, first_three_characters
from flask_login import current_user


main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():

    search_form = SearchForm()

    if search_form.validate_on_submit():
        pass
        # FROM HERE
        # return render_template('search_results.html', search_form=search_form, login_form=LoginForm(),
        #                         register_form=RegisterForm(), logout_form=LogoutForm(), user=current_user,
        #                         format_price=format_price, first_three_characters=first_three_characters)

    login_form = LoginForm()

    register_form = RegisterForm()

    logout_form = LogoutForm()

    properties_and_rooms = get_popular_properties()

    return render_template('index.html', search_form=search_form, login_form=login_form, register_form=register_form,
                            logout_form=logout_form, user=current_user, properties_and_rooms=properties_and_rooms,
                            format_price=format_price, first_three_characters=first_three_characters)
