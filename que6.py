def get_every_other_sublist(lst, start_index, end_index):
    """
    Returns the sublist containing every second element between the given indices.

    Args:
        lst (list): The input list.
        start_index (int): The starting index of the sublist (inclusive).
        end_index (int): The ending index of the sublist (exclusive).

    Returns:
        list: The sublist containing every second element.
    """
    sublist = lst[start_index:end_index:2]
    return sublist


# Example usage
input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_every_other_sublist(input_list, start_index, end_index)
print(result)
