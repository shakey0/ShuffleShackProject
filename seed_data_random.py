from ShuffleShackApp.models.user import User
from ShuffleShackApp.models.property import Property
from ShuffleShackApp.models.room import Room
from ShuffleShackApp.models.booking import Booking
from datetime import date
import random
import string
from sqlalchemy.exc import IntegrityError

from lists import common_baby_names, common_last_names, common_adjectives_for_people, common_email_domains, \
    nationalities, countries, cities, adjectives_for_places
import random


things_to_overlook = ['the city', 'the lake', 'the river', 'the mountains', 'the hills', 'the forest', 'the sea', 'the ocean', 'the beach', 'the countryside', 'the fields', 'the central park', 'the old town', 'the new town', 'the harbour', 'the docks', 'the port', 'the city centre', 'the city lake']


def create_random_users(number_of_users):
    users = []
    used_user_names = set()
    used_emails = set()
    for _ in range(number_of_users):

        if len(users) % 5000 == 0 and len(users) > 0:
            print(f"{len(users)} users have been generated so far.")

        random_first_name = random.choice(common_baby_names)
        random_last_name = random.choice(common_last_names)
        error_breaker = 0
        while error_breaker < 100:
            error_breaker += 1
            random_user_name = f"{random.choice(common_adjectives_for_people)}{random.choice(['', '_', '-'])}{random_first_name.lower()}{random.choice(['', '_', '-'])}{random_last_name[0].lower()}{random.choice(['', '_', '-'])}{random.randint(1, 1000)}"
            if random_user_name not in used_user_names:
                used_user_names.add(random_user_name)
                break
        if error_breaker == 100:
            print('ERROR: Could not create unique username')
            exit()
        error_breaker = 0
        while error_breaker < 100:
            error_breaker += 1
            random_email = f"{random_first_name.lower()}{random.choice(['', '_', '-'])}{random.choice(string.ascii_lowercase)}{random.choice(['', '_', '-'])}{random_last_name.lower()}{random.choice(['', '_', '-'])}{random.randint(1, 1000)}@{random.choice(common_email_domains)}"
            if random_email not in used_emails:
                used_emails.add(random_email)
                break
        if error_breaker == 100:
            print('ERROR: Could not create unique email')
            exit()
        random_phone_number = ''.join(random.choices(string.digits, k=10))

        user = User(
            first_name=random_first_name, 
            last_name=random_last_name, 
            user_name=random_user_name, 
            email=random_email, 
            phone_number=random_phone_number, 
            password=b'secret',
            d_o_b=date(random.randint(1950, 2000), random.randint(1, 12), random.randint(1, 28)),
            nationality=random.choice(nationalities), 
            t_bookings=random.randint(0, 20), 
            no_shows=0, 
            guest_complaints=0, 
            host_complaints=0, 
            is_admin=False
        )
        users.append(user)

    print(f"{len(users)} users have been generated.")
    return users


def create_random_properties(number_of_properties, random_users):

    property_types = ['House', 'Apartment', 'Lodge']
    cancel_periods = [24, 48, 72]
    geographical_words = ['River', 'Central', 'Hillside', 'Seaside', 'Jungle', 'Innercity', 'Old Town']
    stay_words = ['Stay', 'House', 'Lodge', 'Apartment', 'Home', 'Place', 'Cottage', 'Cabin', 'Retreat', 'Residence', 'Mansion', 'Manor']
    street_words = ['Street', 'Road', 'Avenue', 'Lane', 'Drive', 'Place', 'Square', 'Court', 'Terrace', 'Mews', 'Close', 'Crescent', 'Grove', 'Way', 'Walk', 'Hill', 'Park', 'Gardens']
    
    breakfasts = ['Continental', 'Continental', 'Continental', 'Continental', 'Continental', 'Full English', 'Bagel & Tea', 'Bagel & Juice', 'Toast & Cereal', 'Toast & Cereal', 'Cooked Breakfast', 'Buffet', 'Buffet', 'Waffles', 'Pancakes', 'Tea & Toast', 'Toast & Juice']
    breakfast_prices = [0, 0, 0, 0, 0, 500, 600, 700, 800, 900, 1000, 1000, 1200, 1200, 1500]
    lunches = ['Sandwich', 'Salad', 'Soup', 'Pasta', 'Stew', 'Homecooked Meal']
    lunch_prices = [0, 500, 500, 500, 500, 500, 600, 700, 800, 900, 1000, 1500, 2000]
    afternoon_teas = ['Tea & Biscuits', 'Tea & Scones', 'Tea & Croissants']
    afternoon_tea_prices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 300, 400, 500, 600, 700, 800]
    dinners = ['Set Menu', 'BBQ', 'Homecooked Meal']
    dinner_prices = [0, 0, 800, 800, 800, 1000, 1000, 1000, 1500, 2000, 3000, 4000, 5000, 6000]

    airport_transfers = ['Airport transfer per person', 'Airport transfer for up to 4 people']
    airport_transfer_prices = [0, 0, 0, 0, 0, 400, 500, 600, 800, 1000]
    extras = ['Late check-out until 4 pm', 'Cooking class', 'Massage', 'City tour', 'Mine tour', 'Horse riding', 'Bike hire']
    extra_prices = [400, 500, 600, 700, 800, 900, 1000, 1200, 1500, 2000, 3000, 4000]

    location_sayings = ['in the heart of ', 'in the centre of ', 'in the middle of ', 'in the outskirts of ', 'in the suburbs of ', 'in the hills of ', 'on the coast of ', 'on the river of ', 'on the lake of ', 'on the edge of ']

    min_ages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 6, 8, 10, 12, 14, 16, 16, 18, 18]

    properties = []
    for _ in range(number_of_properties):

        if len(properties) % 5000 == 0 and len(properties) > 0:
            print(f"{len(properties)} properties have been generated so far.")

        generated_meals = {}  # FROM HERE GENERATING MEALS

        chance_of_breakfast = random.randint(0, 3)
        if chance_of_breakfast:
            breakfast = random.choice(breakfasts)
            breakfast_price = random.choice(breakfast_prices)
            generated_meals['Breakfast'] = {breakfast: breakfast_price}
            if chance_of_breakfast == 3:
                breakfast = random.choice(breakfasts)
                breakfast_price = random.choice(breakfast_prices)
                generated_meals['Breakfast'] = {breakfast: breakfast_price}
        chance_of_lunch = random.randint(0, 9)
        if chance_of_lunch == 9:
            lunch = random.choice(lunches)
            lunch_price = random.choice(lunch_prices)
            generated_meals['Lunch'] = {lunch: lunch_price}
        chance_of_afternoon_tea = random.randint(0, 9)
        if chance_of_afternoon_tea == 9:
            afternoon_tea = random.choice(afternoon_teas)
            afternoon_tea_price = random.choice(afternoon_tea_prices)
            generated_meals['Afternoon Tea'] = {afternoon_tea: afternoon_tea_price}
        chance_of_dinner = random.randint(0, 4)
        if chance_of_dinner >= 3:
            dinner = random.choice(dinners)
            dinner_price = random.choice(dinner_prices)
            generated_meals['Dinner'] = {dinner: dinner_price}
            if chance_of_dinner == 4:
                dinner = random.choice(dinners)
                dinner_price = random.choice(dinner_prices)
                generated_meals['Dinner'] = {dinner: dinner_price}

        generated_extras = {}  # FROM HERE GENERATING EXTRAS

        chance_of_extras = random.randint(0, 3)
        if chance_of_extras:
            airport_transfer = random.choice(airport_transfers)
            airport_transfer_price = random.choice(airport_transfer_prices)
            generated_extras[airport_transfer] = airport_transfer_price
            if chance_of_extras >= 2:
                extra = random.choice(extras)
                extra_price = random.choice(extra_prices)
                generated_extras[extra] = extra_price
                if chance_of_extras == 3:
                    extra = random.choice(extras)
                    extra_price = random.choice(extra_prices)
                    generated_extras[extra] = extra_price

        chosen_adjective = random.choice(adjectives_for_places)
        if chosen_adjective[0] in ['a', 'e', 'i', 'o', 'u']:
            chosen_adjective = 'An ' + chosen_adjective
        else:
            chosen_adjective = 'A ' + chosen_adjective

        review_food = random.randint(10, 50)
        review_host = random.randint(10, 50)
        review_room = random.randint(10, 50)
        review_comfort = random.randint(10, 50)
        review_location = random.randint(10, 50)
        review_property = random.randint(10, 50)
        review_cleanliness = random.randint(10, 50)
        number_5_stars = random.randint(0, 10)
        number_4_stars = random.randint(0, 10)
        number_3_stars = random.randint(0, 9)
        number_2_stars = random.randint(0, 7)
        number_1_stars = random.randint(0, 5)
        number_of_reviews = number_5_stars + number_4_stars + number_3_stars + number_2_stars + number_1_stars
        review_data = {
            'section_averages': {'food': review_food, 'host': review_host, 'room': review_room, 'comfort': review_comfort, 'location': review_location, 'property': review_property, 'cleanliness': review_cleanliness},
            'average_rating': (review_food + review_host + review_room + review_comfort + review_location + review_property + review_cleanliness) // 7,
            'number_of_reviews': number_of_reviews,
            'ratings': {'5': number_5_stars, '4': number_4_stars, '3': number_3_stars, '2': number_2_stars, '1': number_1_stars}
        }
        
        generated_host_pets = {}

        chance_of_pets = random.randint(0, 9)
        if chance_of_pets >= 8:
            number_of_dogs = random.randint(1, 3)
            generated_host_pets['Dog'] = number_of_dogs
        elif 7 <= chance_of_pets <= 8:
            number_of_cats = random.randint(1, 3)
            generated_host_pets['Cat'] = number_of_cats

        generated_guest_pets = {}

        chance_of_pets = random.randint(0, 19)
        if chance_of_pets >= 18:
            generated_guest_pets['Dog'] = True
        if chance_of_pets >= 17:
            generated_guest_pets['Cat'] = True

        if not generated_guest_pets:
            pets_messsage = random.choice(['We do not allow pets.', 'We only allow service pets.', 'Guests cannot bring pets.'])
        else:
            if generated_guest_pets.get('Dog') and generated_guest_pets.get('Cat'):
                pets_messsage = random.choice(['We welcome all pets.', 'We welcome dogs and cats. Please inform us by adding it to your booking.', 'We welcome all pets. Please inform us by adding it to your booking.'])
            else:
                pets_messsage = random.choice(['We welcome cats. Please inform us by adding it to your booking.', 'We welcome cats.'])

        country = random.choice(countries)
        property_type = random.choice(property_types)
        city=random.choice(cities[country])

        property = Property(
            display_image_url='test_property_image.webp',
            country=country,
            city=city,
            address_1 = f"{random.randint(1, 999)} {city} {random.choice(street_words)}",
            address_2 = f"{random.choice(['', random.choice(['Central ' + city, 'City Centre', 'Outer ' + city])])}",
            address_3 = "",
            postcode = ''.join(random.choices(string.ascii_uppercase, k=2)) + ''.join(random.choices(string.digits, k=2)) + ' ' + ''.join(random.choices(string.digits, k=1)) + ''.join(random.choices(string.ascii_uppercase, k=2)),
            phone_number=''.join(random.choices(string.digits, k=10)),
            name=f"{city} {random.choice(geographical_words)} {random.choice(stay_words)}",
            type=property_type,
            description=f"{chosen_adjective} {property_type.lower()} {random.choice(location_sayings)}{city} overlooking {random.choice(things_to_overlook)}.",
            check_in_from = random.randint(12, 16),
            check_in_to = random.randint(20, 27),
            check_out = random.randint(9, 13),
            cancel_period = random.choice(cancel_periods),
            meals=generated_meals,
            min_age=random.choice(min_ages),
            min_stay=random.randint(1, 3),
            host_pets=generated_host_pets,
            guest_pets=generated_guest_pets,
            pets_notice=pets_messsage,
            extras=generated_extras,
            review_data=review_data,
            user_id=random.choice(range(1, len(random_users) + 1))
        )
        properties.append(property)

    print(f"{len(properties)} properties have been generated.")
    return properties


def create_random_rooms(number_of_rooms, random_properties):

    common_floors = ['Ground', '1', '2', '3', 'Attic']
    more_floors = ['Ground', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', 'Garden', 'Yard', 'Field']
    
    bed_types = ['Single', 'Queen', 'Double', 'King', 'Super King']
    unusual_bed_types = ['Bunk', 'Triple Bunk', 'Floor Space']
    bed_capacity = {'Single': 1, 'Queen': 2, 'Double': 2, 'King': 2, 'Super King': 2,
                    'Bunk': 2, 'Triple Bunk': 3, 'Floor Space': 1}
    
    room_names = ['', '', 'Room', 'Room', 'Room', 'Room', 'Room', 'Room', 'Room', 'Room', 'Suite', 'Suite', 'Suite', 'Suite', 'Villa', 'Apartment', 'Cabin', 'House', 'Flat', 'Studio', 'Chalet', 'Cottage', 'Bungalow']
    unusual_room_names = ['Room', 'Suite', 'Villa', 'Apartment', 'Cabin', 'House', 'Flat', 'Studio', 'Chalet', 'Cottage', 'Bungalow', 'Penthouse', 'Condo', 'Guesthouse', 'Tent', 'Camping Spot', 'Treehouse', 'Houseboat', 'Barn', 'Hut', 'Dome House', 'Lighthouse', 'Windmill']
    room_name_adjectives = ['Luxury ', 'Comfortable ', 'Cosy ', 'Spacious ', 'Modern ', 'Rustic ', 'Traditional ', 'Quaint ', 'Charming ', 'Stylish ', 'Elegant ', 'Gorgeous ', 'Lovely ', 'Delightful ', 'Enchanting ', 'Exquisite ', 'Superb ', 'Magnificent ', 'Impressive ', 'Grand ', 'Majestic ', 'Prestigious ']
    view_adjectives = ['a wonderful', 'a fantastic', 'a gorgeous', 'a beautiful', 'a stunning', 'a breathtaking', 'an amazing', 'a spectacular', 'a lovely', 'a delightful', 'an enchanting', 'an exquisite', 'a superb', 'a magnificent', 'an impressive', 'a grand', 'a majestic', 'a prestigious']

    available_days_6_combos = ['Mon,Tue,Wed,Thu,Fri,Sat', 'Mon,Tue,Wed,Thu,Fri,Sun', 'Mon,Tue,Wed,Thu,Sat,Sun', 'Mon,Tue,Wed,Fri,Sat,Sun', 'Mon,Tue,Thu,Fri,Sat,Sun', 'Mon,Wed,Thu,Fri,Sat,Sun', 'Tue,Wed,Thu,Fri,Sat,Sun']
    available_days_6_weekends = ['Mon,Tue,Wed,Thu,Fri,Sat', 'Tue,Wed,Thu,Fri,Sat,Sun', 'Wed,Thu,Fri,Sat,Sun,Mon', 'Thu,Fri,Sat,Sun,Mon,Tue', 'Fri,Sat,Sun,Mon,Tue,Wed']
    available_days_5_combos = ['Mon,Tue,Wed,Thu,Fri', 'Mon,Tue,Wed,Thu,Sat', 'Mon,Tue,Wed,Thu,Sun', 'Mon,Tue,Wed,Fri,Sat', 'Mon,Tue,Wed,Fri,Sun', 'Mon,Tue,Thu,Fri,Sat', 'Mon,Tue,Thu,Fri,Sun', 'Mon,Tue,Fri,Sat,Sun', 'Mon,Wed,Thu,Fri,Sat', 'Mon,Wed,Thu,Fri,Sun', 'Mon,Wed,Thu,Sat,Sun', 'Mon,Wed,Fri,Sat,Sun', 'Mon,Thu,Fri,Sat,Sun', 'Tue,Wed,Thu,Fri,Sat', 'Tue,Wed,Thu,Fri,Sun', 'Tue,Wed,Thu,Sat,Sun', 'Tue,Wed,Fri,Sat,Sun', 'Tue,Thu,Fri,Sat,Sun', 'Wed,Thu,Fri,Sat,Sun']
    available_days_5_weekends = ['Tue,Wed,Thu,Fri,Sat', 'Wed,Thu,Fri,Sat,Sun', 'Thu,Fri,Sat,Sun,Mon', 'Fri,Sat,Sun,Mon,Tue']
    available_days_4_combos = ['Mon,Tue,Wed,Thu', 'Mon,Tue,Wed,Fri', 'Mon,Tue,Wed,Sat', 'Mon,Tue,Wed,Sun', 'Mon,Tue,Thu,Fri', 'Mon,Tue,Thu,Sat', 'Mon,Tue,Thu,Sun', 'Mon,Tue,Fri,Sat', 'Mon,Tue,Fri,Sun', 'Mon,Tue,Sat,Sun', 'Mon,Wed,Thu,Fri', 'Mon,Wed,Thu,Sat', 'Mon,Wed,Thu,Sun', 'Mon,Wed,Fri,Sat', 'Mon,Wed,Fri,Sun', 'Mon,Wed,Sat,Sun', 'Mon,Thu,Fri,Sat', 'Mon,Thu,Fri,Sun', 'Mon,Thu,Sat,Sun', 'Mon,Fri,Sat,Sun', 'Tue,Wed,Thu,Fri', 'Tue,Wed,Thu,Sat', 'Tue,Wed,Thu,Sun', 'Tue,Wed,Fri,Sat', 'Tue,Wed,Fri,Sun', 'Tue,Wed,Sat,Sun', 'Tue,Thu,Fri,Sat', 'Tue,Thu,Fri,Sun', 'Tue,Thu,Sat,Sun', 'Tue,Fri,Sat,Sun', 'Wed,Thu,Fri,Sat', 'Wed,Thu,Fri,Sun', 'Wed,Thu,Sat,Sun', 'Wed,Fri,Sat,Sun', 'Thu,Fri,Sat,Sun']
    available_days_4_weekends = ['Thu,Fri,Sat,Sun', 'Fri,Sat,Sun,Mon']
    available_days_3_combos = ['Mon,Tue,Wed', 'Mon,Tue,Thu', 'Mon,Tue,Fri', 'Mon,Tue,Sat', 'Mon,Tue,Sun', 'Mon,Wed,Thu', 'Mon,Wed,Fri', 'Mon,Wed,Sat', 'Mon,Wed,Sun', 'Mon,Thu,Fri', 'Mon,Thu,Sat', 'Mon,Thu,Sun', 'Mon,Fri,Sat', 'Mon,Fri,Sun', 'Mon,Sat,Sun', 'Tue,Wed,Thu', 'Tue,Wed,Fri', 'Tue,Wed,Sat', 'Tue,Wed,Sun', 'Tue,Thu,Fri', 'Tue,Thu,Sat', 'Tue,Thu,Sun', 'Tue,Fri,Sat', 'Tue,Fri,Sun', 'Tue,Sat,Sun', 'Wed,Thu,Fri', 'Wed,Thu,Sat', 'Wed,Thu,Sun', 'Wed,Fri,Sat', 'Wed,Fri,Sun', 'Wed,Sat,Sun', 'Thu,Fri,Sat', 'Thu,Fri,Sun', 'Thu,Sat,Sun', 'Fri,Sat,Sun']
    available_days_3_weekends = ['Thu,Fri,Sat','Fri,Sat,Sun']

    extra_beds = ['Fold out bed', 'Extra bed']
    sleeping_bags = ['Sleeping bag', 'Sleeping bag for sofa', 'Sleeping bag and mat']
    extra_bed_prices = [0, 500, 1000, 1000, 1200, 1200, 1500, 1500, 2000, 3000]
    sleeping_bag_prices = [0, 0, 400, 500, 500, 600, 600, 700, 700, 800, 800, 900, 900, 1000, 1000, 1200, 1500, 2000]

    rooms = []
    for _ in range(number_of_rooms):

        if len(rooms) % 5000 == 0 and len(rooms) > 0:
            print(f"{len(rooms)} rooms have been generated so far.")

        generated_beds = {}

        number_of_bed_types = random.randint(0, 4)
        if number_of_bed_types != 2:
            number_of_bed_types = 1
        for _ in range(number_of_bed_types):
            bed_types_list = random.randint(0, 19)
            if bed_types_list == 19:
                bed_type = random.choice(unusual_bed_types)
            else:
                bed_type = random.choice(bed_types)
            number_of_beds_for_bed_type = random.choice([1, 1, 1, 1, 1, 1, 1, 1, 2])
            if bed_type in unusual_bed_types or bed_type == 'Single':
                number_of_beds_for_bed_type = random.choice([1, 1, 2, 2, 2, 2, 3, 4])
            generated_beds[bed_type] = number_of_beds_for_bed_type * bed_capacity[bed_type]

        if 'Super King' in generated_beds and sum(generated_beds.values()) <= 3:
            room_name_type = 'Super King '
        elif 'King' in generated_beds and sum(generated_beds.values()) <= 3:
            room_name_type = 'King '
        elif 'Queen' in generated_beds and sum(generated_beds.values()) <= 3:
            room_name_type = 'Queen '
        elif 'Double' in generated_beds and sum(generated_beds.values()) <= 3:
            room_name_type = 'Double '
        elif ('Single' in generated_beds or 'Bunk' in generated_beds) and sum(generated_beds.values()) == 4:
            room_name_type = 'Quad '
        elif ('Single' in generated_beds or 'Triple Bunk' in generated_beds) and sum(generated_beds.values()) == 3:
            room_name_type = 'Triple '
        elif ('Single' in generated_beds or 'Bunk' in generated_beds) and sum(generated_beds.values()) == 2:
            room_name_type = 'Twin '
        elif 'Single' in generated_beds and sum(generated_beds.values()) == 1:
            room_name_type = 'Single '
        elif sum(generated_beds.values()) > 3:
            room_name_type = 'Family '
        else:
            room_name_type = ''

        if sum(generated_beds.values()) >= 4:
            has_bathroom = random.choice([True, True, True, True, True, True, True, True, True, True, True, True, False])
        else:
            has_bathroom = random.choice([True, True, False])

        available_days_chooser = random.randint(0, 95)
        if available_days_chooser >= 12:
            available_days = 'All'
        elif available_days_chooser >= 9:
            available_days = random.choice([random.choice(available_days_6_combos), random.choice(available_days_6_weekends)])
        elif available_days_chooser >= 6:
            available_days = random.choice([random.choice(available_days_5_combos), random.choice(available_days_5_weekends)])
        elif available_days_chooser >= 3:
            available_days = random.choice([random.choice(available_days_4_combos), random.choice(available_days_4_weekends)])
        else:
            available_days = random.choice([random.choice(available_days_3_combos), random.choice(available_days_3_weekends)])
        
        max_guests = sum(generated_beds.values()) + random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 4, 5, 6])
        
        generated_extras = {}

        if max_guests > sum(generated_beds.values()):
            extra_beds_chooser = random.choice([random.choice(extra_beds), random.choice(sleeping_bags)])
            if not 'bed' in extra_beds_chooser:
                generated_extras[extra_beds_chooser] = random.choice(sleeping_bag_prices)
                if random.randint(0, 1) == 1:
                    extra_beds_chooser = random.choice(extra_beds)
                    generated_extras[extra_beds_chooser] = random.choice(extra_bed_prices)
            else:
                generated_extras[extra_beds_chooser] = random.choice(extra_bed_prices)
        if random.randint(0, 1) == 1:
            generated_extras['Cot'] = random.choice([0, 0, 0, 0, 0, 0, 0, 0, 500, 500, 500, 500, 1000, 1000, 1500])

        error_breaker = 0
        while error_breaker < 100:
            error_breaker += 1
            room_name = random.choice(["", random.choice(room_name_adjectives)]) + room_name_type + random.choice(['Room', random.choice(room_names), random.choice(unusual_room_names)])
            if room_name:
                break
        if error_breaker == 100:
            print('ERROR: Could not create unique username')
            exit()

        prep = "An" if room_name[0] in ['A', 'E', 'I', 'O', 'U'] else "A"
        
        room = Room(
            start_date=date(2023, random.randint(5, 12), random.randint(1, 28)),
            end_date=date(2024, random.randint(1, 4), random.randint(1, 28)),
            available_days=available_days,
            name=room_name,
            floor=random.choice([random.choice(common_floors), random.choice(common_floors), random.choice(common_floors), random.choice(common_floors), random.choice(common_floors), random.choice(more_floors)]),
            description=f"{prep} {room_name.lower()} with {random.choice(view_adjectives)} view of {random.choice(things_to_overlook)}.",
            beds=generated_beds,
            max_guests=max_guests,
            has_bathroom=has_bathroom,
            has_tv=random.choice([True, True, True, True, True, False]),
            extras=generated_extras,
            price=sum([random.randint(1000, 4000) for _ in range(max_guests)]) + random.randint(0, 4000),
            premium=random.choice([0, random.randint(1000, 4000)]),
            property_id=random.choice(range(1, len(random_properties) + 1))
        )
        rooms.append(room)

    print(f"{len(rooms)} rooms have been generated.")
    return rooms


def init_random_data(db, number_of_users, number_of_properties, number_of_rooms):

    from flask import Flask
    from ShuffleShackApp.config import DevelopmentConfig

    results = []
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    with app.app_context():

        results = []

        attempt, max_attempts, random_users = 0, 5, []
        while attempt < max_attempts and number_of_users > 0:

            try:
                random_users = create_random_users(number_of_users)
                db.session.add_all(random_users)
                db.session.commit()
                results.append(f"Added {number_of_users} random users to the database.")
                break

            except IntegrityError as error:
                db.session.rollback()
                attempt += 1
                print(f"Error: {error}")

        if len(results) == 0:
            results.append(f"Failed to add {number_of_users} random users to the database after {max_attempts} attempts.")
        
        attempt, max_attempts, random_properties = 0, 5, []
        while attempt < max_attempts and number_of_properties > 0:

            try:
                random_properties = create_random_properties(number_of_properties, random_users)
                db.session.add_all(random_properties)
                db.session.commit()
                results.append(f"Added {number_of_properties} random properties to the database.")
                break

            except IntegrityError as error:
                db.session.rollback()
                attempt += 1
                print(f"Error: {error}")
        
        if len(results) == 1:
            results.append(f"Failed to add {number_of_properties} random properties to the database after {max_attempts} attempts.")
        
        attempt, max_attempts, random_rooms = 0, 5, []
        while attempt < max_attempts and number_of_rooms > 0:

            try:
                random_rooms = create_random_rooms(number_of_rooms, random_properties)
                db.session.add_all(random_rooms)
                db.session.commit()
                results.append(f"Added {number_of_rooms} random rooms to the database.")
                break

            except IntegrityError as error:
                db.session.rollback()
                attempt += 1
                print(f"Error: {error}")
        
        if len(results) == 2:
            results.append(f"Failed to add {number_of_rooms} random rooms to the database after {max_attempts} attempts.")
        
        # attempt, max_attempts, random_bookings = 0, 5, []
        # while attempt < max_attempts and number_of_bookings > 0:

        #     try:
        #         random_bookings = create_random_bookings(number_of_bookings, random_users, random_rooms)
        #         db.session.add_all(random_bookings)
        #         db.session.commit()
        #         results.append(f"Added {number_of_bookings} random bookings to the database.")
        #         break

        #     except IntegrityError:
        #         db.session.rollback()
        #         attempt += 1
        #         print(f"Attempt {attempt} failed due to a unique constraint violation. Retrying...")
        
        # if len(results) == 3:
        #     results.append(f"Failed to add {number_of_bookings} random bookings to the database after {max_attempts} attempts.")

        db.session.remove()
    return results
