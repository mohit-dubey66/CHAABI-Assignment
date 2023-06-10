def switch_key_value(dictionary):
    """
    Switches the positions of keys and values in the dictionary.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        dict: The dictionary with keys and values switched.
    """
    return {value: key for key, value in dictionary.items()}


#Test case
input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

result = switch_key_value(input_dict)
print(result)
