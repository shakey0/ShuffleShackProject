from ShuffleShackApp.models.user import User
from ShuffleShackApp.models.property import Property
from ShuffleShackApp.models.room import Room
from datetime import date


def init_user(db):
    test_user = User(
        first_name='John',
        last_name='Doe',
        user_name='john_doe',
        email='john@example.com',
        phone_number='1234567890',
        password=b'secret',
        d_o_b=date(1990, 1, 1),
        nationality='Testland',
        t_bookings=5,
        no_shows=1,
        guest_complaints=0,
        host_complaints=0,
        is_admin=False
    )
    db.session.add(test_user)
    db.session.commit()


def init_property(db):
    test_property = Property(
        country='Testland',
        city='Testville',
        address_1='1 Test Street',
        address_2='Test District',
        address_3='Test County',
        postcode='TE5 7PC',
        phone_number='0987654321',
        name='Test Property',
        type='House',
        description='A test property',
        check_in_from=12,
        check_in_to=14,
        check_out=10,
        cancel_period=24,
        meals={'Breakfast': {'Croissant & Coffee': 0}},
        min_age=18,
        min_stay=1,
        host_pets={'Cat': 1},
        guest_pets={},
        pets_notice='Guests cannot bring pets. Our cat hates other animals.',
        extras={'Evening tour of Verona': 800},
        review_data={
            'average_rating': 45,  # Multiplied by 10 to avoid floating point errors
            'number_of_reviews': 10,
            'ratings': {
                '5': 5,
                '4': 3,
                '3': 1,
                '2': 1,
                '1': 0
            }, 'section_averages': {
                'food': 45,
                'host': 47,
                'room': 43,
                'comfort': 44,
                'location': 46,
                'property': 45,
                'cleanliness': 45}
        },
        user_id=1
    )
    db.session.add(test_property)
    db.session.commit()


def init_room(db):
    test_room = Room(
        start_date=date(2023, 2, 15),
        end_date=date(2024, 2, 14),
        available_days='Mon,Tue,Wed,Thu,Fri',
        name='Cozy Suite',
        floor='1',
        description='A cozy and comfortable suite with modern amenities',
        beds={'Queen': 2, 'Super King': 2},
        max_guests=6,
        has_bathroom=True,
        has_tv=True,
        extras={"Fold out bed": 3000, "Cot": 1000},
        price=31000,  # Multiplied by 100 to avoid floating point errors
        premium=8000,  # Multiplied by 100 to avoid floating point errors
        property_id=1
    )
    db.session.add(test_room)
    db.session.commit()
