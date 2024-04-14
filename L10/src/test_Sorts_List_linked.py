'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = '2024-03-20'
'''


# Imports
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(0, SIZE):
        values.append(Number(i))
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """

    # your code here
    values = List()
    for i in range(SIZE - 1, -1, -1):
        values.append(Number(i))
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """

    # your code here
    lists = []
    for i in range(0, TESTS):
        list2 = List()
        for j in range(0, SIZE):
            random_number = Number(random.randint(0, XRANGE))
            list2.append(random_number)
        lists.append(list2)
    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    Sorts.swaps = 0
    Number.comparisons = 0
    sorted_list = create_sorted()
    print("{}".format(title), end='')
    func(sorted_list)
    comparisons_sorted = Number.comparisons
    num_swaps_sorted = Sorts.swaps
    Number.comparisons = 0
    Sorts.swaps = 0

    reversed_list = create_reversed()
    func(reversed_list)
    comparisons_reversed = Number.comparisons
    num_swaps_reversed = Sorts.swaps
    Number.comparisons = 0
    Sorts.swaps = 0

    random_list = create_randoms()
    total_comparisons_random = 0
    for _list in random_list:
        func(_list)
        total_comparisons_random += Number.comparisons
        Number.comparisons = 0
    average_comparisons_random = total_comparisons_random / len(random_list)
    avg_swaps_random = Sorts.swaps / len(random_list)
    Sorts.swaps = 0

    print("\t{:<8.0f} {:<8.0f} {:<8.0f}\t{:<8.0f} {:<8.0f} {:<8.0f}".format(comparisons_sorted, comparisons_reversed,
                                                                            average_comparisons_random, num_swaps_sorted,
                                                                            num_swaps_reversed, avg_swaps_random))
    return
