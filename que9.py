"""
Q9. Write a func that takes 3 args:
    from_date - string representing a date in the form of 'yy-mm-dd'
    to_date - string representing a date in the form of 'yy-mm-dd'
    difference - int
    Returns True if from_date and to_date are less than difference days away from each other, else
    returns False.
"""


from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    date_format = '%y-%m-%d'

    # Convert string dates to datetime objects
    from_datetime = datetime.strptime(from_date, date_format)
    to_datetime = datetime.strptime(to_date, date_format)

    # Calculate the difference between the dates
    date_difference = abs((to_datetime - from_datetime).days)

    # Compare the difference with the specified value
    if date_difference < difference:
        return True
    else:
        return False

# Test case
from_date = '21-05-10'
to_date = '21-05-20'
difference = 15
result = check_date_difference(from_date, to_date, difference)
print(result)
