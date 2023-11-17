from ShuffleShackApp.models.user import User
from datetime import date


def test_user_creation(test_app, test_client, seed_test_database):

    user = User.query.filter_by(user_name='john_doe').first()

    assert user is not None
    assert user.id == 1
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert user.user_name == 'john_doe'
    assert user.email == 'john@example.com'
    assert user.phone_number == '1234567890'
    assert user.password == b'secret'
    assert user.d_o_b == date(1990, 1, 1)
    assert user.nationality == 'Testland'
    assert user.t_bookings == 5
    assert user.no_shows == 1
    assert user.guest_complaints == 0
    assert user.host_complaints == 0
    assert user.is_admin == False

    assert user.__eq__(User.query.filter_by(user_name='john_doe').first()) is True
    assert user.__repr__() == '<User 1 john_doe>'
