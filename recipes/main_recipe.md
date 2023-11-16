# 1. User requirements

#### User as host:
**Can do:**
- can add properties for hosting >> properties table
- can add different kinds of rooms to each property >> rooms table
- can add the specific check in times as well as the time to check out by >> check_in_from, check_in_to, check_out columns in properties table
- can specify the amount of days in advanced the booking can be cancelled >> cancel_period in properties table
- can specify which meals are provided and the type and price of those meals (if meals are free, a message saying the number of free meals will be included - this will be calculated by the number of beds/floor_spaces) >> meals column in properties table
- can set a minimum age for guests >> min_age column in properties table
- can set a minimum amount of days rooms must be booked for (1-7) >> min_stay column in properties table
- can specify their pets >> host pets column in in properties table
- can specify which pets guests are allowed to bring and have a pets notice >> guest_pets, pets_notice columns in properties table
- can set the available dates (from and to) on a room >> start_date, end_date in rooms table
- can mark which days of the week are available >> available_days in rooms table
- can blank out periods by selecting "Add a period of unavailability", which creates a false booking >> will be done with Python code
- can select which beds are in a room and how many of each >> beds column (JSON) in rooms table
- can specify the max_guests allowed in a room >> max_guests column in rooms table
- can sets the price and premium price for weekends (Friday and Saturday nights) >> price, premium columns in rooms table
- get a message when a guest has booked at the property >> seen_by_host in bookings table >> Python code will search all bookings with the property_id and then pick out any that have seen_by_host set to False
- can click 'seen' on a new booking to set seen_by_host to True
- MENTION - can modify the start_date, end_date, or available days to clash with a guest's booking >> this will not affect the since these features will only be read by the code when the booking is being made
- can cancel a guest's booking (changes the status to cancelled) >> status column in bookings table
- can mark a booking as no_show the day after supposed check_in (this must delete the entry in rooms_bookings to allow the room to be available) >> will be done with Python code, no_shows column in users table
- can reply to a review >> review_reply in bookings table
- can make a complaint about a guest who has stayed at their property (an admin will then review this), this can also be about an abusive review >> complaints table, type column which will be set to guest_complaint, Python code to check that the guest_user_id is in a booking with the property_id, and the host_user_id is in that property, the date must also be within 7 days of the end_date of the booking
- can make a complaint about a guest who is abusing the booking process >> complaints table, type column which will be set to booking_abuse, Python code to check that the guest_user_id is in a booking with the property_id, and the host_user_id is in that property, the status of the booking must also be cancelled or no_show and the date must be within 7 days of the end_date of the booking
- can view all previous and future bookings associated with a room or property in order of time_made, upcoming, past >> time_made column in bookings, Python code will ensure a booking cannot be deleted until the property has been deleted
**Can do with restrictions:**
- once there are no bookings associated with a room, or all the bookings are before the current date plus 7 days, the user can delete the room >> Python code will first delete the entry in rooms_bookings to allow this
- once there are no rooms associated with a property, the user can delete the property
- once there are no properties associated with the user, the user can delete themselves (their account)
**Cannot do:**
- delete a guest's booking >> Python code will not allow this
- set the status of a booking to cancelled on the day or after the guest's stay is complete >> Python code will not allow this
- change the floor, beds or bathroom aspects of a room since it is misleading (another room must be created) >> Python code will not allow this

#### User as guest:
- can see a list of properties when going onto the website >> properties table
- can choose a country and city to view properties in >> country and city column in properties
- can choose dates to book and number of people with a tick box for floor_is_okay >> start_date, end_date, available_days, beds, max_guests in rooms table
- can star properties for future viewing >> users_properties
- can set filters for properties and rooms together: type, check_in_after_XX, includes_breakfast (free), accepts_children (under 16), allows_pets (cats, dogs*, all), bed_types, bathroom, tv, price_per_night >> type, check_in_to, meals, min_age, guest_pets in properties table; beds, has_bathroom, has_tv, price, premium in rooms table
- can see all rooms that have future availability in a property, and can only book rooms that have availability on the user's search dates >> will be done with Python code
- can see all the reviews for a property in order of most_recent, best, worst, or search for words in reviews >> will be done with Python code
- can like a review >> users_bookings table
- can make a booking (the host must be notified) >> bookings table, seen_by_host column
- can add multiple rooms to a booking >> rooms_bookings table
- can amend the check_in, meals, guest_info, has_pets parts of a booking (any extra prices for meals will be added) >> seen_by_host in bookings tables, will be done with Python code (the host must be notified)
- can add a review on the day of the booking end_date >> review_ratings in bookings table, will be done with Python code
- can make a complaint about a host whose property the user has stayed at (an admin will then review this) >> complaints table, type column which will be set to host_complaint, Python code to check that the guest_user_id is in a booking with the property_id, and the host_user_id is in that property, the date must also be within 7 days of the end_date of the booking
- can report a bogus property >> complaints table, type column which will be set to bogus_property_'property_id'
- can view all previous and future bookings associated with a room or property >> Python code will ensure a booking cannot be deleted until the user has been deleted
- can cancel a booking before the cancel period >> cancel_period in properties table, status in bookings table
**Can do with restrictions:**
- can delete cancelled or no_show bookings 7 days after cancellation >> will be done with Python code
**Cannot do:**
- cancel a booking that is after the cancel_period >> cancel_period in properties, will be done with Python code
- change the dates of a booking
- review a property before the check_out date, review a property if the booking was cancelled or no_show >> will be done with Python code

#### User as admin:
- MENTION - a token must be generated upon login and safely stored, this token will last for 30 minutes, it will be checked for all actions that require admin permissions
- can delete a booking related to a false room
- can delete a false room
- can delete a false property
- can delete a false user
- can see all complaints
- can see a list of unaddressed complaints >> addressed column in complaints table
- can set addressed in a complaint to True
- can increase the number of guest_complaints and host_complaints >> guest_complaints, host_complaints in users table
- can remove a review >> Python code will reset the review_ratings column for the entry
- can remove a review_reply >> Python code will update 'removed' to the review_reply column for the entry

#### Delete Considerations
- if a property is deleted, the system will check for bookings with the property_id, and then those bookings will be checked for users with the user_id, and if any users are not found, the booking will be deleted
- if a user is deleted, the system will check for bookings with the user_id, and then those bookings will be checked for properties with the property_id, and if any properties are not found, the booking will be deleted
- if a user is deleted, the system will check for complaints with the user_id, and then those complaints will be checked for users with the other user_id, and if any of the other users are not found, the complaint will be deleted

#### Other Considerations
- to avoid unnecessary computations, review averages for a property must be calculated each time a review is added >> review_data column in properties, will be done with Python code


# 2. Table data and properties

**users:** id, first_name, last_name, user_name, email, phone_number, password, d_o_b, nationality, t_bookings, no_shows, guest_complaints, host_complaints, is_admin

**complaints:** id, type, text, date, addressed, guest_user_id, host_user_id

**properties:** id, country, city, address_1, address_2, address_3, postcode, phone_number, name, type, description, check_in_from, check_in_to, check_out, cancel_period, meals, min_age, min_stay, host_pets, guest_pets, pets_notice, extras (JSON), review_data, user_id
(many properties can be added to a user THEREFORE a property is owned by a user, DELETE RESTRICT)

**rooms:** id, start_date, end_date, available_days, name, floor, description, beds, max_guests, has_bathroom, has_tv, extras (JSON), price, premium, property_id
(many rooms can be added to a property THEREFORE a room is owned by a property, DELETE RESTRICT)

**bookings:** id, is_real, time_made, start_date, end_date, check_in, meals, guest_info, has_pets, room_info, property_info, status, seen_by_host, messages (JSON), review_ratings, review_reply, property_id, user_id
(many bookings can be added to a room AND many rooms can be added to a booking THEREFORE a join table is required between bookings and rooms)

**rooms_bookings:** room_id, booking_id
(DELETE RESTRICT; DELETE CASCADE)

**users_properties:** user_id, property_id
(so a user can 'star' a property and find it again, a join table between users and properties is needed)
(DELETE CASCADE; DELETE CASCADE)

**users_bookings:** user_id, booking_id
(so a user can 'like' a review, a join table between users and bookings is needed)
(DELETE CASCADE; DELETE CASCADE)


# 3. Repository & Model Classes

### Retrieval Requirements

1. When a user first enters the site unauthenticated, they can see a list of popular properties from around the world >>
    

2. When a user enters the start_date, end_date, no_of_guests, can_sleep_on_floor, country and city and presses search, they can see a list of properties with available rooms on those dates and available beds/spaces in that location >>
    

3. When a user sets the following filters - type, check_in_after_XX, includes_breakfast (free), accepts_children (under 16), allows_pets (cats, dogs*, all), bed_types, bathroom, tv, price_per_night - the above method will be added to accordingly >>
    
