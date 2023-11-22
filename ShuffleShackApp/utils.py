import datetime


def format_price(price):
    return f'{price/100:.2f}'


def first_three_characters(user_name):
    return user_name[:3]


def description_limiter(description):
    if len(description) <= 50:
        return description
    description = description[:50]
    after_last_space = description.rfind(' ')
    description = description[:after_last_space]
    if description[-1] == ',' or description[-1] == '.':
        description = description[:-1]
    return description + '...'


def room_name_checker(room_name):
    if 'room' in room_name.lower():
        return room_name
    return room_name + ' Room'


bed_capacity = {
    'Single': 1,
    'Queen': 2,
    'Double': 2,
    'King': 2,
    'Super King': 2,
    'Bunk': 2,
    'Triple Bunk': 3,
    'Floor Space': 1,
}

def format_beds(bed_tuple_dict_items):
    formatted_bed_strings = []
    for bed_tuple_data in bed_tuple_dict_items:
        bed_type = bed_tuple_data[0]
        number_of_beds_for_bed_type = bed_tuple_data[1]// bed_capacity[bed_type]
        if number_of_beds_for_bed_type == 1:
            formatted_bed_strings.append(f"{number_of_beds_for_bed_type} {bed_type} bed")
        else:
            formatted_bed_strings.append(f"{number_of_beds_for_bed_type} {bed_type} beds")
    return formatted_bed_strings


def get_dates(start_date, end_date):
    date_list = []
    current_date = start_date
    while current_date < end_date:
        date_list.append(current_date)
        current_date += datetime.timedelta(days=1)
    return date_list
