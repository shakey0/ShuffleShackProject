from flask import Blueprint
from ShuffleShackApp.extensions import db
from ShuffleShackApp.models.user import User
from ShuffleShackApp.models.property import Property
from ShuffleShackApp.models.room import Room
from ShuffleShackApp.models.booking import Booking
from sqlalchemy.sql.expression import func
from flask import render_template

main = Blueprint('main', __name__)


def get_popular_properties():
    # Subquery to get maximum property ID for each city with average rating >= 40
    subquery = db.session.query(
            func.max(Property.id).label('max_id'),
            Property.city
        ) \
        .filter(func.cast(Property.review_data['average_rating'], db.Integer) >= 40) \
        .group_by(Property.city) \
        .subquery()

    # Main query to join with the subquery and get property details
    properties = db.session.query(Property) \
        .join(subquery, Property.id == subquery.c.max_id) \
        .order_by(func.random()) \
        .limit(30) \
        .all()
    return properties


@main.route('/')
def index():

    # user = User.query.filter_by(id=1).first()
    # print(f'user: {user}')
    # property = Property.query.filter_by(id=1).first()
    # print(property)
    # room = Room.query.filter_by(id=1).first()
    # print(room)

    return f'{[property.name for property in get_popular_properties()]}'
