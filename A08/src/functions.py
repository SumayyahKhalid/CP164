'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 14, 2023
'''

# Imports
from Letter import Letter
# Constants


def do_comparisons(file_variable, bst):
    """
    -------------------------------------------------------
    Retrieves every letter in file_variable from bst. Generates
    comparisons in bst objects. Each Letter object in bst contains
    the number of comparisons found by searching for that Letter
    object in file_variable.
    Use: do_comparisons(file_variable, bst)
    -------------------------------------------------------
    Parameters:
        file_variable - the already open file containing data to evaluate (file)
        bst - the binary search tree containing 26 Letter objects
            to retrieve data from (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    # Zeroes out all comparison values in tree nodes
    for node in bst:
        node.comparisons = 0

    # your code here
    file = file_variable.read()
    for i in file:
        if i.isalpha():
            letter = Letter(i.upper())
            bst.retrieve(letter)
    return


def comparison_total(bst):
    """
    -------------------------------------------------------
    Sums the comparison values of all Letter objects in bst.
    Use: total = comparison_total(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        total - the total of all comparison fields in the bst
            Letter objects (int)
    -------------------------------------------------------
    """
    total = 0
    for node in bst.inorder():
        total += node.comparisons
    return total


def letter_table(bst):
    """
    -------------------------------------------------------
    Prints a table of letter counts for each Letter object in bst.
    Use: letter_table(bst)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
    Returns:
        None
    -------------------------------------------------------
    """
    print("Letter Count/Percent Table")
    print(" ")
    inorder = bst.inorder()
    total = 0
    for letter in inorder:
        total += letter.count
    print("Total Count: {:,}".format(total))
    print(" ")
    print("Letter  Count        %")
    print("-" * 22)
    for letter in inorder:
        percent = (letter.count / total) * 100
        print("{:>5s} {:>6d} {:>7.2f} %".format(
            letter.letter, letter.count, percent))


def insert_test(bst, values):
    """
    -------------------------------------------------------
    Inserts values into bst. Prints the number of comparisons
    made by each insert operation.
    Use: insert(bst, values)
    -------------------------------------------------------
    Parameters:
        bst - a binary search tree of Letter objects (BST)
        values - a list of values to insert into bst (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for value in values:
        letter = Letter(value)
        print(f"Inserting {value} ...", end="")
        bst.insert(letter)
        print(f" {letter.comparisons} comparisons.")
    return

