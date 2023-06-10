def sort_list_of_dicts(list_of_dicts, sort_key):
    """
    Sorts a list of dictionaries based on the specified key.

    Args:
        list_of_dicts (list): List of dictionaries.
        sort_key (str): Key to sort the list of dictionaries.

    Returns:
        list: Sorted list of dictionaries.
    """
    sorted_list = sorted(list_of_dicts, key=lambda x: x[sort_key])
    return sorted_list


#Test case
input_list = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

sorted_list_by_fruit = sort_list_of_dicts(input_list, "fruit")
print(sorted_list_by_fruit)

sorted_list_by_color = sort_list_of_dicts(input_list, "color")
print(sorted_list_by_color)
