from ShuffleShackApp.models.property import Property


def test_property_creation(test_app, test_client, seed_test_database):

    property = Property.query.filter_by(name='Test Property').first()

    assert property is not None
    assert property.id == 1
    assert property.country == 'Testland'
    assert property.city == 'Testville'
    assert property.address_1 == '1 Test Street'
    assert property.address_2 == 'Test District'
    assert property.address_3 == 'Test County'
    assert property.postcode == 'TE5 7PC'
    assert property.phone_number == '0987654321'
    assert property.name == 'Test Property'
    assert property.type == 'House'
    assert property.description == 'A test property'
    assert property.check_in_from == 12
    assert property.check_in_to == 24
    assert property.check_out == 10
    assert property.cancel_period == 24
    assert property.meals == {'Breakfast': {'Croissant & Coffee': 0}}
    assert property.min_age == 0
    assert property.min_stay == 1
    assert property.host_pets == {'Cat': 1}
    assert property.guest_pets == {}
    assert property.pets_notice == 'Guests cannot bring pets. Our cat hates other animals.'
    assert property.extras == {'Evening tour of Verona': 800}
    assert property.review_data == {
        'average_rating': 45,
        'number_of_reviews': 10,
        'ratings': {'5': 5, '4': 3, '3': 1, '2': 1, '1': 0},
        'section_averages': {'food': 45, 'host': 47, 'room': 43, 'comfort': 44, 'location': 46, 'property': 45, 'cleanliness': 45}
    }
    assert property.user_id == 1
    assert 'Breakfast' in property.meals
    assert [key for key, value in property.meals['Breakfast'].items() if value == 0] == ['Croissant & Coffee']
    assert [key for key, value in property.meals['Breakfast'].items() if value > 0] == []
    assert [key for key, value in property.meals['Breakfast'].items() if value == 0]
    assert not [key for key, value in property.meals['Breakfast'].items() if value > 0]
    assert property.host_pets
    assert 'Cat' in property.host_pets
    assert not property.guest_pets
    assert property.extras

    assert property.__eq__(Property.query.filter_by(name='Test Property').first()) is True
    assert property.__repr__() == '<Property 1 Test Property>'
