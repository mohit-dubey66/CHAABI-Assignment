"""
Q10. Of date and days
    Write a func that takes 2 args:
    date - string representing a date in the form of 'yy-mm-dd'
    n - integer
    Returns the string representation of date n days before 'date'
    E.g. f('16-12-10', 11) should return '16-11-29'
"""

from datetime import datetime, timedelta

def get_date_n_days_before(date, n):
    date_format = '%y-%m-%d'

    # Convert string date to datetime object
    date_obj = datetime.strptime(date, date_format)

    # Calculate the timedelta for n days
    timedelta_obj = timedelta(days=n)

    # Subtract timedelta from the date
    new_date_obj = date_obj - timedelta_obj

    # Format the new date as a string
    new_date_str = new_date_obj.strftime(date_format)

    return new_date_str


# Test case
date = '16-12-10'
n = 11
result = get_date_n_days_before(date, n)
print(result)
