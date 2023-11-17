from ShuffleShackApp.models.user import User
from ShuffleShackApp.models.property import Property
from ShuffleShackApp.models.room import Room
from ShuffleShackApp.models.booking import Booking
from datetime import date, datetime


def init_users(db):
    users = [
        User(first_name='John', last_name='Doe', user_name='john_doe', email='john@example.com', phone_number='1234567890', password=b'secret', d_o_b=date(1990, 1, 1), nationality='Testland', t_bookings=5, no_shows=1, guest_complaints=0, host_complaints=0, is_admin=False),
        User(first_name='Alice', last_name='Smith', user_name='alice_smith', email='alice@example.com', phone_number='2345678901', password=b'secret', d_o_b=date(1991, 2, 2), nationality='Testland', t_bookings=3, no_shows=0, guest_complaints=0, host_complaints=0, is_admin=True),
        User(first_name='Bob', last_name='Brown', user_name='bob_brown', email='bob@example.com', phone_number='3456789012', password=b'secret', d_o_b=date(1992, 3, 3), nationality='Testland', t_bookings=4, no_shows=2, guest_complaints=0, host_complaints=0, is_admin=False),
        User(first_name='Brian', last_name='Taylor', user_name='brian_taylor', email='brian@example.com', phone_number='2456789012', password=b'secret', d_o_b=date(1988, 4, 4), nationality='Testland', t_bookings=2, no_shows=0, guest_complaints=0, host_complaints=2, is_admin=False),
        User(first_name='Charlotte', last_name='Green', user_name='charlotte_green', email='charlotte@example.com', phone_number='2567890123', password=b'secret', d_o_b=date(1993, 5, 5), nationality='Testland', t_bookings=6, no_shows=0, guest_complaints=1, host_complaints=0, is_admin=False),
        User(first_name='David', last_name='Evans', user_name='david_evans', email='david@example.com', phone_number='2678901234', password=b'secret', d_o_b=date(1987, 6, 6), nationality='Testland', t_bookings=4, no_shows=2, guest_complaints=0, host_complaints=0, is_admin=False),
        User(first_name='Emily', last_name='Harris', user_name='emily_harris', email='emily@example.com', phone_number='2789012345', password=b'secret', d_o_b=date(1992, 7, 7), nationality='Testland', t_bookings=5, no_shows=1, guest_complaints=0, host_complaints=1, is_admin=False),
        User(first_name='Frank', last_name='Martin', user_name='frank_martin', email='frank@example.com', phone_number='2890123456', password=b'secret', d_o_b=date(1986, 8, 8), nationality='Testland', t_bookings=3, no_shows=0, guest_complaints=2, host_complaints=0, is_admin=False),
        User(first_name='Grace', last_name='Clark', user_name='grace_clark', email='grace@example.com', phone_number='2901234567', password=b'secret', d_o_b=date(1994, 9, 9), nationality='Testland', t_bookings=7, no_shows=1, guest_complaints=0, host_complaints=0, is_admin=False),
        User(first_name='Irene', last_name='Adler', user_name='irene_adler', email='irene@example.com', phone_number='9876543210', password=b'secret', d_o_b=date(1989, 9, 9), nationality='Testland', t_bookings=7, no_shows=0, guest_complaints=1, host_complaints=0, is_admin=False)
    ]
    db.session.add_all(users)
    db.session.commit()


def init_properties(db):
    test_property1 = Property(
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
        check_in_to=24,
        check_out=10,
        cancel_period=24,
        meals={'Breakfast': {'Croissant & Coffee': 0}},
        min_age=0,
        min_stay=1,
        host_pets={'Cat': 1},
        guest_pets={},
        pets_notice='Guests cannot bring pets. Our cat hates other animals.',
        extras={'Evening tour of Verona': 800},
        review_data={
            'average_rating': 45,  # Multiplied by 10 to avoid floating point errors
            'number_of_reviews': 10,
            'ratings': {'5': 5, '4': 3, '3': 1, '2': 1, '1': 0},
            'section_averages': {'food': 45, 'host': 47, 'room': 43, 'comfort': 44, 'location': 46, 'property': 45, 'cleanliness': 45}
        },
        user_id=1
    )

    test_property2 = Property(
        country='Sampleland',
        city='Example City',
        address_1='123 Example Lane',
        address_2='Sample District',
        address_3='Example County',
        postcode='EX4 6PL',
        phone_number='0123456789',
        name='Sample Property',
        type='Apartment',
        description='A sample property for testing',
        check_in_from=14,
        check_in_to=3,
        check_out=11,
        cancel_period=48,
        meals={'Breakfast': {'Bagel & Tea': 0, 'Full English': 500}},
        min_age=8,
        min_stay=2,
        host_pets={},
        guest_pets={'Dog': True},
        pets_notice='Guests can bring dogs. Please inform us by adding it to your booking.',
        extras={'City tour': 1200, 'Airport transfer for up to 4 people': 400, 'Late check-out until 4 pm': 2000, 'Cooking class': 1500, 'Massage': 2000},
        review_data={
            'average_rating': 40,
            'number_of_reviews': 5,
            'ratings': {'5': 2, '4': 2, '3': 0, '2': 1, '1': 0},
            'section_averages': {'food': 40, 'host': 42, 'room': 38, 'comfort': 39, 'location': 41, 'property': 40, 'cleanliness': 40}
        },
        user_id=6
    )

    db.session.add(test_property1)
    db.session.add(test_property2)
    db.session.commit()


def init_rooms(db):
    rooms = [
        Room(
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
            price=31000,
            premium=8000,
            property_id=1
        ),
        Room(
            start_date=date(2023, 3, 1),
            end_date=date(2024, 2, 28),
            available_days='All',
            name='Modern Room',
            floor='2',
            description='A modern room with elegant design',
            beds={'King': 2},
            max_guests=2,
            has_bathroom=True,
            has_tv=True,
            extras={},
            price=11000,
            premium=2000,
            property_id=2
        ),
        Room(
            start_date=date(2023, 3, 1),
            end_date=date(2024, 2, 28),
            available_days='All',
            name='Modern Room',
            floor='2',
            description='A modern room with elegant design',
            beds={'King': 2},
            max_guests=2,
            has_bathroom=True,
            has_tv=True,
            extras={},
            price=11000,
            premium=2000,
            property_id=2
        ),
        Room(
            start_date=date(2023, 5, 1),
            end_date=date(2024, 4, 30),
            available_days='Fri,Sat,Sun',
            name='Simple Room',
            floor='Ground',
            description='Ideal for weekend getaways with a kitchenette and dining area',
            beds={'Double': 2},
            max_guests=4,
            has_bathroom=False,
            has_tv=True,
            extras={"Sleeping bag for sofa": 800},
            price=9000,
            premium=0,
            property_id=2
        ),
        Room(
            start_date=date(2023, 6, 1),
            end_date=date(2024, 6, 1),
            available_days='Mon,Thu,Fri,Sat,Sun',
            name='Cosy Barn',
            floor='Ground',
            description='Our lovely converted barn with a rustic feel',
            beds={'Single': 4},
            max_guests=8,
            has_bathroom=True,
            has_tv=True,
            extras={"Fold out bed": 1500, "Sleeping bag and mat": 800},
            price=14000,
            premium=2000,
            property_id=2
        )
    ]

    db.session.add_all(rooms)
    db.session.commit()


def init_bookings(db):
    bookings = [
        Booking(  # BOOKING 1
            is_real=True,
            time_made=datetime(2023, 5, 21, 9, 34, 23),
            start_date=date(2023, 6, 5),
            end_date=date(2023, 6, 8),
            check_in=14,
            inclusions={},
            guest_info={
                "1": {"first_name": "Bob", "last_name": "Brown", "nationality": "Testland", "age": 31},
                "2": {"first_name": "Sally", "last_name": "Brown", "nationality": "Testland", "age": 32}
            },
            has_pets={},
            room_info={
                "1": {
                    "total_price": 93000,
                    "name": "Cozy Suite",
                    "floor": "1",
                    "beds": {"Queen": 2, "Super King": 2},
                    "bathroom": True
                }
            },
            property_info={
                "country": "Testland", 
                "city": "Testville", 
                "address_1": "1 Test Street",
                "address_2": "Test District", 
                "address_3": "Test County", 
                "postcode": "TE5 7PC",
                "phone_number": "0987654321", 
                "name": "Test Property", 
                "check_in_from": 12,
                "check_in_to": 14, 
                "check_out": 10, 
                "cancel_period": 24, 
                "min_age": 0, 
                "host_pets": {"Cat": 1},
                "guest_pets": {}, 
                "overall_review": 45
            },
            status='active',
            seen_by_host='seen',
            messages={
                "1": {"user_id": 1, "time": "2023-05-21T14:34:23", "message": "Hello Bob! Look forward to seeing you! James"},
                "2": {"user_id": 3, "time": "2023-05-22T08:47:51", "message": "Hello James! Same!"}
            },
            review_ratings={},
            review_reply='',
            property_id=1,
            user_id=3
        ),
        Booking(  # BOOKING 2
            is_real=True,
            time_made=datetime(2023, 5, 22, 21, 20, 3),
            start_date=date(2023, 5, 29),
            end_date=date(2023, 6, 1),
            check_in=20,
            inclusions={},
            guest_info={
                "1": {"first_name": "Emily", "last_name": "Harris", "nationality": "Testland", "age": 31}
            },
            has_pets={},
            room_info={
                "1": {
                    "total_price": 70000,
                    "name": "Cozy Suite",
                    "floor": "1",
                    "beds": {"Queen": 2, "Super King": 2},
                    "bathroom": True
                }
            },
            property_info={
                "country": "Testland", 
                "city": "Testville", 
                "address_1": "1 Test Street",
                "address_2": "Test District", 
                "address_3": "Test County", 
                "postcode": "TE5 7PC",
                "phone_number": "0987654321", 
                "name": "Test Property", 
                "check_in_from": 12,
                "check_in_to": 14, 
                "check_out": 10, 
                "cancel_period": 24, 
                "min_age": 0, 
                "host_pets": {"Cat": 1},
                "guest_pets": {}, 
                "overall_review": 45
            },
            status='reviewed',
            seen_by_host='seen',
            messages={
                "1": {"user_id": 1, "time": "2023-05-23T08:37:09", "message": "Hello Emily! Look forward to seeing you! James"}
            },
            review_ratings={
                "overall": 40, "room": 4, "comfort": 5, "property": 4, "cleanliness": 4, 
                "host": 3, "food": 5, "location": 3, "things_liked": "The porridge was amazing!", 
                "things_disliked": "It was a bit noisy!", "total_stays": 4
            },
            review_reply='Glad you liked the porridge! Sorry about the noise!',
            property_id=1,
            user_id=7
        ),
        Booking(  # BOOKING 3
            is_real=True,
            time_made=datetime(2023, 5, 22, 21, 55, 44),
            start_date=date(2023, 6, 3),
            end_date=date(2023, 6, 18),
            check_in=15,
            inclusions={
                "Massage": [
                    {"date": "2023-06-05", "quantity": 2, "total_price": 4000},
                    {"date": "2023-06-10", "quantity": 2, "total_price": 4000}
                ],
                "Airport transfer for up to 4 people": [
                    {"date": "2023-06-06", "quantity": 1, "total_price": 400}
                ]
            },
            guest_info={
                "1": {"first_name": "Brian", "last_name": "Taylor", "nationality": "Testland", "age": 35},
                "2": {"first_name": "Elivra", "last_name": "Taylor", "nationality": "Bolivian", "age": 33},
                "3": {"first_name": "Federico", "last_name": "Santino", "nationality": "Peruvian", "age": 34},
                "4": {"first_name": "Michella", "last_name": "Santino", "nationality": "Peruvian", "age": 29}
            },
            has_pets={},
            room_info={
                "2": {
                    "total_price": 162000,
                    "name": "Modern Room",
                    "floor": "2",
                    "beds": {"King": 2},
                    "bathroom": True
                },
                "3": {
                    "total_price": 162000,
                    "name": "Modern Room",
                    "floor": "2",
                    "beds": {"King": 2},
                    "bathroom": True
                }
            },
            property_info={
                "country": "Sampleland",
                "city": "Example City",
                "address_1": "123 Example Lane",
                "address_2": "Sample District",
                "address_3": "Example County",
                "postcode": "EX4 6PL",
                "phone_number": "0123456789",
                "name": "Sample Property",
                "check_in_from": 14,
                "check_in_to": 22,
                "check_out": 11,
                "cancel_period": 48,
                "min_age": 8,
                "host_pets": {},
                "guest_pets": {"Dog": 1},
                "overall_review": 40
            },
            status='reviewed',
            seen_by_host='seen',
            messages={
                "1": {"user_id": 4, "time": "2023-05-22T22:01:22", "message": "Hi! Look forward to staying with you!"},
                "2": {"user_id": 6, "time": "2023-05-23T06:03:49", "message": "Hello Brian! Look forward to meeting you."}
            },
            review_ratings={
                "overall": 50, "room": 5, "comfort": 5, "property": 5, 
                "cleanliness": 5, "host": 5, "food": 5, "location": 5, 
                "things_liked": "Everything!", "total_stays": 2
            },
            review_reply='',
            property_id=2,
            user_id=4
        ),
        Booking(  # BOOKING 4
            is_real=False,
            time_made=datetime(2023, 5, 24, 13, 51, 33),
            start_date=date(2023, 6, 19),
            end_date=date(2023, 9, 24),
            check_in=0,
            inclusions={},
            guest_info={},
            has_pets={},
            room_info={
                "2": {},
                "3": {},
                "4": {},
                "5": {}
            },
            property_info={},
            status="false",
            seen_by_host="false",
            messages={},
            review_ratings={},
            review_reply='',
            property_id=2,
            user_id=6
        ),
        Booking(  # BOOKING 5
            is_real=True,
            time_made=datetime(2023, 6, 27, 19, 12, 14),
            start_date=date(2023, 6, 30),
            end_date=date(2023, 7, 3),
            check_in=18,
            inclusions={
                "City tour": [
                    {"date": "2023-07-01", "quantity": 7, "total_price": 8400}
                ],
                "Cooking class": [
                    {"date": "2023-07-02", "quantity": 7, "total_price": 10500}
                ],
                "Massage": [
                    {"date": "2023-06-30", "quantity": 4, "total_price": 8000},
                    {"date": "2023-07-01", "quantity": 2, "total_price": 4000},
                    {"date": "2023-07-02", "quantity": 4, "total_price": 8000}
                ],
                "Airport transfer for up to 4 people": [
                    {"date": "2023-06-30", "quantity": 2, "total_price": 800},
                    {"date": "2023-07-03", "quantity": 2, "total_price": 800}
                ],
                "Fold out bed": [
                    {"date": "2023-06-30", "quantity": 3, "total_price": 4500},
                    {"date": "2023-07-01", "quantity": 3, "total_price": 4500},
                    {"date": "2023-07-02", "quantity": 3, "total_price": 4500}
                ]
            },
            guest_info={
                "1": {"first_name": "Irene", "last_name": "Adler", "nationality": "Testland", "age": 34},
                "2": {"first_name": "Dan", "last_name": "Adler", "nationality": "Testland", "age": 39},
                "3": {"first_name": "Cindy", "last_name": "Adler", "nationality": "Testland", "age": 15},
                "4": {"first_name": "Sophie", "last_name": "Adler", "nationality": "Testland", "age": 13},
                "5": {"first_name": "Peter", "last_name": "Adler", "nationality": "Testland", "age": 12},
                "6": {"first_name": "Lucy", "last_name": "Adler", "nationality": "Testland", "age": 10},
                "7": {"first_name": "Jordan", "last_name": "Adler", "nationality": "Testland", "age": 8}
            },
            has_pets={},
            room_info={
                "5": {
                    "total_price": 46000,
                    "name": "Cosy Barn",
                    "floor": "Ground",
                    "beds": {"Single": 4},
                    "bathroom": True
                }
            },
            property_info={
                "country": "Sampleland",
                "city": "Example City",
                "address_1": "123 Example Lane",
                "address_2": "Sample District",
                "address_3": "Example County",
                "postcode": "EX4 6PL",
                "phone_number": "0123456789",
                "name": "Sample Property",
                "check_in_from": 14,
                "check_in_to": 22,
                "check_out": 11,
                "cancel_period": 48,
                "min_age": 8,
                "host_pets": {},
                "guest_pets": {"Dog": 1},
                "overall_review": 40
            },
            status='reviewed',
            seen_by_host='seen',
            messages={
                "1": {"user_id": 10, "time": "2023-06-27T19:22:30", "message": "Hi! Look forward to coming!"},
                "2": {"user_id": 6, "time": "2023-06-28T06:07:03", "message": "Hello Irene! Look forward to seeing you soon!"}
            },
            review_ratings={
                "overall": 40, "room": 4, "comfort": 4, "property": 5, 
                "cleanliness": 4, "host": 5, "food": 3, "location": 3, 
                "things_liked": "The hosts were so welcoming!", "things_disliked": "The bathroom was a bit small!", 
                "total_stays": 7
            },
            review_reply='',
            property_id=2,
            user_id=10
        )
    ]

    db.session.add_all(bookings)
    db.session.flush()

    for booking in bookings:
        room_ids = [int(room_id) for room_id in booking.room_info.keys()]
        rooms = Room.query.filter(Room.id.in_(room_ids)).all()
        booking.rooms = rooms

    db.session.commit()
