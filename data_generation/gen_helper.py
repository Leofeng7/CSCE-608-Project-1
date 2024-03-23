import random
import string
from datetime import datetime, timedelta

def generate_random_word(length):
    word = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    return word

def generate_random_date(start_year=2000, end_year=2024, date_format="YYYY::MM::DD"):
    # Convert the date_format to something datetime can understand
    date_format = date_format.replace("YYYY", "%Y").replace("MM", "%m").replace("DD", "%d")
    
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    
    # Calculate the difference between start and end dates
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    
    # Generate a random number of days to add to the start date
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    
    # Return the formatted random date
    return random_date.strftime(date_format)

def generate_entity_type():
    rand = random.randint(0, 1)
    if not rand:
        return 'Post'
    else:
        return 'Comment'