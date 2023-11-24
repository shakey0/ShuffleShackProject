from ShuffleShackApp.extensions import db
from ShuffleShackApp.models.property import Property
from ShuffleShackApp.models.room import Room
from ShuffleShackApp.models.booking import Booking, rooms_bookings
from ShuffleShackApp.utils import get_dates
from sqlalchemy import func, and_, or_, not_
from sqlalchemy.orm import aliased
import datetime


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

    properties_and_rooms = db.session.query(
            Property,
            Room
        ) \
        .join(subquery, Property.id == subquery.c.max_id) \
        .join(Room, Property.id == Room.property_id) \
        .join(lowest_price_room_subquery, (Room.property_id == lowest_price_room_subquery.c.property_id) & (Room.price == lowest_price_room_subquery.c.min_price)) \
        .order_by(func.random()) \
        .limit(30) \
        .all()

    already_appended = []
    return [(property, [room], '', room.price) for property, room in properties_and_rooms if property.id not in already_appended and not already_appended.append(property.id)]


BookingAlias = aliased(Booking)
RoomBookingAlias = aliased(rooms_bookings)

def get_search_properties(check_in, check_out, city, number_of_guests):
    
    query = (
        db.session.query(Property, Room)
        .join(Room, Property.id == Room.property_id)
        .outerjoin(RoomBookingAlias, Room.id == RoomBookingAlias.c.room_id)
        .outerjoin(BookingAlias, and_(
            RoomBookingAlias.c.booking_id == BookingAlias.id,
            or_(
                BookingAlias.start_date.between(check_in, check_out),
                BookingAlias.end_date.between(check_in, check_out)
            )
        ))
        .filter(Property.city == city)
        .filter(or_(BookingAlias.id == None, and_(
            not_(BookingAlias.start_date.between(check_in, check_out)),
            not_(BookingAlias.end_date.between(check_in, check_out))
        )))
    )

    properties_with_rooms = query.all()

    check_in = datetime.datetime.strptime(check_in, "%Y-%m-%d").date()
    check_out = datetime.datetime.strptime(check_out, "%Y-%m-%d").date()

    available_properties_and_rooms = []
    for property, room in properties_with_rooms:
        if room.available_days == 'All':
            available_properties_and_rooms.append((property, room))
        else:
            all_dates = get_dates(check_in, check_out)
            room.available_days = room.available_days.split(',')
            available_dates = [date for date in all_dates if date.strftime('%a') in room.available_days]
            if len(all_dates) == len(available_dates):
                available_properties_and_rooms.append((property, room))

    bed_space_properties_and_rooms = []
    exact_properties, more_properties, less_properties = [], [], []
    less_bed_space_properties_and_rooms = []

    for property, room in available_properties_and_rooms:
        total_bed_spaces = sum(room.beds.values())
        # print(total_bed_spaces)
        if total_bed_spaces == number_of_guests:
            bed_space_properties_and_rooms.append((property, [room], 'Exact', room.price))
            exact_properties.append(property.id)
        elif total_bed_spaces > number_of_guests:
            bed_space_properties_and_rooms.append((property, [room], f'More{total_bed_spaces - number_of_guests}', room.price))
            more_properties.append(property.id)
        elif total_bed_spaces < number_of_guests and room.max_guests >= number_of_guests:
            bed_space_properties_and_rooms.append((property, [room], f'Less{number_of_guests - total_bed_spaces}', room.price))
            less_bed_space_properties_and_rooms.append((property, room))
            less_properties.append(property.id)
        else:
            less_bed_space_properties_and_rooms.append((property, room))
            less_properties.append(property.id)
    
    for property, room in less_bed_space_properties_and_rooms:
        if property.id in exact_properties:
            continue
        if property.id in more_properties and property.id not in less_properties:
            continue
        exact_ps, more_ps, less_ps = [], [], []
        rooms_for_property = []
        rooms_for_property.append(room)
        for p, r in less_bed_space_properties_and_rooms:
            if p.id in exact_ps:
                continue
            if p.id in more_ps and p.id not in less_ps:
                continue
            if p.id == property.id:
                if r.id == room.id:
                    continue
                rooms_for_property.append(r)
                for room in rooms_for_property:
                    print(room.name, room.beds)
                if sum([sum(x.beds.values()) for x in rooms_for_property]) == number_of_guests:
                    bed_space_properties_and_rooms.append((property, [x for x in rooms_for_property], 'Exact', sum([x.price for x in rooms_for_property])))
                    exact_ps.append(property.id)
                    print('EXACT\n')
                elif sum([sum(x.beds.values()) for x in rooms_for_property]) > number_of_guests:
                    bed_space_properties_and_rooms.append((property, [x for x in rooms_for_property], f'More{sum([sum(x.beds.values()) for x in rooms_for_property]) - number_of_guests}', sum([x.price for x in rooms_for_property])))
                    more_ps.append(property.id)
                    print('MORE\n')
                elif sum([sum(x.beds.values()) for x in rooms_for_property]) < number_of_guests and sum([x.max_guests for x in rooms_for_property]) >= number_of_guests:
                    bed_space_properties_and_rooms.append((property, [x for x in rooms_for_property], f'Less{number_of_guests - sum([sum(x.beds.values()) for x in rooms_for_property])}', sum([x.price for x in rooms_for_property])))
                    less_ps.append(property.id)
                    print('LESS\n')

    bed_space_properties_and_rooms.sort(key=lambda property_room: property_room[3])
    bed_space_properties_and_rooms.sort(key=lambda property_room: property_room[2])
    favoured_properties_and_rooms = []
    return [(property, room, accuracy, price) for property, room, accuracy, price in bed_space_properties_and_rooms if property.id not in favoured_properties_and_rooms and not favoured_properties_and_rooms.append(property.id)]
