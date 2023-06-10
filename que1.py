def selection_sort(lst):
    """
    Q1. Get your basics right - Implement selection sort algorithm in python.
    The function accepts a list in the input and returns a sorted list.
    E.g.    Input f1([5,416,54,21,6135,15,741]) should
            Return [5, 15, 21, 54, 416, 741, 6135]

    Args:
        lst (list): An unsorted list of elements.

    Returns:
        list: The sorted list in ascending order.
    """
    for i in range(len(lst)):
        
        # Find the minimum element in the unsorted part of the list
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        # Swap the minimum element with the first unsorted element
        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst

