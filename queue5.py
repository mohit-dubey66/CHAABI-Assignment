def compare_lists(list1, list2):
    """
    Compares two lists and returns the common elements and non-common elements.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.

    Returns:
        tuple: A tuple containing the common elements and non-common elements.
    """
    common_elements = list(set(list1) & set(list2))
    non_common_elements = list(set(list1) ^ set(list2))
    return common_elements, non_common_elements


# Test case
mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]

common, non_common = compare_lists(mainstream, must_watch)
print(common)
print(non_common)
