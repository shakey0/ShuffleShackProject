from ShuffleShackApp.models.room import Room
from datetime import date


def test_room_creation(test_app, test_client, seed_test_database):

    room_name_part = 'suite'.lower()
    room = Room.query.filter(Room.name.ilike(f"%{room_name_part}%")).first()

    assert room is not None
    assert room.id == 1
    assert room.start_date == date(2023, 2, 15)
    assert room.end_date == date(2024, 2, 14)
    assert room.available_days == 'Mon,Tue,Wed,Thu,Fri'
    assert room.name == 'Cozy Suite'
    assert room.floor == '1'
    assert room.description == 'A cozy and comfortable suite with modern amenities'
    assert room.beds == {'Queen': 2, 'Super King': 2}
    assert room.max_guests == 6
    assert room.has_bathroom is True
    assert room.has_tv is True
    assert room.extras == {"Fold out bed": 3000, "Cot": 1000}
    assert room.price == 31000
    assert room.premium == 8000
    assert room.property_id == 1
    assert 'Super King' in room.beds
    assert 'Fold out bed' in room.extras
    assert room.extras['Fold out bed'] != 0
    assert 'Cot' in room.extras
    assert room.extras['Cot'] > 0
    assert [booking.id for booking in room.bookings] == [1, 2]

    assert room.__eq__(Room.query.filter_by(name='Cozy Suite').first()) is True
    assert room.__repr__() == '<Room 1 Cozy Suite>'
