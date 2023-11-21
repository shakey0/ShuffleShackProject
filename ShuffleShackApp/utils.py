import datetime


def format_price(price):
    return f'{price/100:.2f}'


def first_three_characters(user_name):
    return user_name[:3]


def description_limiter(description):
    if len(description) <= 45:
        return description
    description = description[:45]
    after_last_space = description.rfind(' ')
    description = description[:after_last_space]
    return description + '...'


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

def divide_capacity_for_bed_type(bed_tuple_dict_items):
    bed_tuple_data = list(bed_tuple_dict_items)[0]
    print(bed_tuple_data)  # FROM HERE !!!!!!!!!!!!!!!!!!!!!!
    return (bed_tuple_data[0], bed_capacity[bed_tuple_data[0]] / bed_tuple_data[1])


def get_dates(start_date, end_date):
    date_list = []
    current_date = start_date
    while current_date < end_date:
        date_list.append(current_date)
        current_date += datetime.timedelta(days=1)
    return date_list
