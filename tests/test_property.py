from ShuffleShackApp.models.property import Property


def test_property_creation(test_app, test_client, seed_test_database):

    property = Property.query.filter_by(name='Innsbruck City Stay').first()

    assert property is not None
    assert property.id == 1
    assert property.display_image_url == 'test_property_image.webp'
    assert property.country == 'Austria'
    assert property.city == 'Innsbruck'
    assert property.address_1 == '5 Feldstrasse'
    assert property.address_2 == 'Innenstadt'
    assert property.address_3 == ''
    assert property.postcode == '6020'
    assert property.phone_number == '591 123 4567'
    assert property.name == 'Innsbruck City Stay'
    assert property.type == 'Apartment'
    assert property.description == 'A cozy apartment in the heart of Innsbruck'
    assert property.check_in_from == 15
    assert property.check_in_to == 0
    assert property.check_out == 11
    assert property.cancel_period == 48
    assert property.meals == {'Breakfast': {'Croissant & Coffee': 0}}
    assert property.min_age == 0
    assert property.min_stay == 1
    assert property.host_pets == {'Cat': 1}
    assert property.guest_pets == {}
    assert property.pets_notice == 'Guests cannot bring pets. Our cat hates other animals.'
    assert property.extras == {'Tour vor die Stadt': 800}
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

    assert property.__eq__(Property.query.filter_by(name='Innsbruck City Stay').first()) is True
    assert property.__repr__() == '<Property 1 Innsbruck City Stay>'
