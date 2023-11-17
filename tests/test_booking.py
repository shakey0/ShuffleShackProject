from ShuffleShackApp.models.booking import Booking
from datetime import date, datetime


def test_booking_creation(test_app, test_client, seed_test_database):

    booking = Booking.query.filter_by(id=3).first()

    assert booking is not None
    assert booking.id == 3
    assert booking.is_real is True
    assert booking.time_made == datetime(2023, 5, 22, 21, 55, 44)
    assert booking.start_date == date(2023, 6, 3)
    assert booking.end_date == date(2023, 6, 18)
    assert booking.check_in == 15
    assert booking.inclusions == {
        "Massage": [
            {"date": "2023-06-05", "quantity": 2, "total_price": 4000},
            {"date": "2023-06-10", "quantity": 2, "total_price": 4000}
        ],
        "Airport transfer for up to 4 people": [
            {"date": "2023-06-06", "quantity": 1, "total_price": 400}
        ]
    }
    assert booking.guest_info == {
        "1": {"first_name": "Brian", "last_name": "Taylor", "nationality": "Testland", "age": 35},
        "2": {"first_name": "Elivra", "last_name": "Taylor", "nationality": "Bolivian", "age": 33},
        "3": {"first_name": "Federico", "last_name": "Santino", "nationality": "Peruvian", "age": 34},
        "4": {"first_name": "Michella", "last_name": "Santino", "nationality": "Peruvian", "age": 29}
    }
    assert booking.has_pets == {}
    assert booking.room_info == {
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
    }
    assert booking.property_info == {
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
    }
    assert booking.status == 'reviewed'
    assert booking.seen_by_host == 'seen'
    assert booking.messages == {
        "1": {"user_id": 4, "time": "2023-05-22T22:01:22", "message": "Hi! Look forward to staying with you!"},
        "2": {"user_id": 6, "time": "2023-05-23T06:03:49", "message": "Hello Brian! Look forward to meeting you."}
    }
    assert booking.review_ratings == {
        "overall": 50, "room": 5, "comfort": 5, "property": 5, 
        "cleanliness": 5, "host": 5, "food": 5, "location": 5, 
        "things_liked": "Everything!", "total_stays": 2
    }
    assert booking.review_reply == ''
    assert booking.property_id == 2
    assert booking.user_id == 4
    assert [date.fromisoformat(inclusion['date']) for inclusion in booking.inclusions['Massage']] == [date(2023, 6, 5), date(2023, 6, 10)]
    assert all(inclusion['total_price'] > 0 for inclusion in booking.inclusions['Massage'])
    assert not any(inclusion['total_price'] == 0 for inclusion in booking.inclusions['Massage'])
    assert not any(guest['age'] < 18 for guest in booking.guest_info.values())
    assert all(bed == 'King' for bed in booking.room_info['2']['beds'])
    assert booking.property_info['country'] == 'Sampleland'
    assert 'guest_pets' in booking.property_info
    assert not booking.property_info['host_pets']
    assert booking.property_info['guest_pets']

    assert booking.__eq__(Booking.query.filter_by(id=3).first()) is True
    assert booking.__repr__() == f'<Booking 3 reviewed>'


def test_booking_prices_total(test_app, test_client, seed_test_database):

    booking = Booking.query.filter_by(id=3).first()

    assert sum(room['total_price'] for room in booking.room_info.values()) == 324000
    assert sum(inclusion['total_price'] for inclusion_list in booking.inclusions.values() for inclusion in inclusion_list) == 8400


def test_false_booking(test_app, test_client, seed_test_database):

    false_booking = Booking.query.filter_by(status="false").first()

    assert false_booking is not None
    assert false_booking.id == 4
    assert false_booking.is_real is False
    assert false_booking.time_made == datetime(2023, 5, 24, 13, 51, 33)
    assert false_booking.start_date == date(2023, 6, 19)
    assert false_booking.end_date == date(2023, 9, 24)
    assert false_booking.check_in == 0
    assert false_booking.inclusions == {}
    assert false_booking.guest_info == {}
    assert false_booking.has_pets == {}
    assert false_booking.room_info == {"2": {}, "3": {}, "4": {}, "5": {}}
    assert false_booking.property_info == {}
    assert false_booking.status == "false"
    assert false_booking.seen_by_host == "false"
    assert false_booking.messages == {}
    assert false_booking.review_ratings == {}
    assert false_booking.review_reply == ''
    assert false_booking.property_id == 2
    assert false_booking.user_id == 6
