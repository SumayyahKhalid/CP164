'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 14, 2023
'''


# Imports

# Constants
vowels = "aeiou"


def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    ans = 0

    if x < 0 or y < 0:
        ans = x - y
    else:
        ans = recurse(x-1, y) + recurse(x, y-1)

    return ans


def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    if m % n == 0:
        ans = n
    else:
        ans = gcd(n, m % n)

    return ans


def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    count = 0

    if not s:
        count = 0
    elif s[0].lower() in vowels:
        count = 1 + vowel_count(s[1:])
    else:
        count = vowel_count(s[1:])

    return count


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """
    if power == 0:
        ans = 1
    elif power > 0:
        ans = base * to_power(base, power - 1)
    else:
        ans = 1 / to_power(base, -power)

    return ans


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome = False

    if len(s) < 2:
        palindrome = True
    elif not s[0].isalpha():
        palindrome = is_palindrome(s[1:])
    elif not s[-1].isalpha():
        palindrome = is_palindrome(s[:-1])
    else:
        palindrome = (s[0].lower() == s[-1].lower() and
                      is_palindrome(s[1:-1]))

    return palindrome


def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    new_set = []

    if not bag:
        new_set = []
    else:
        first = bag[0]
        bag_without_first = []
        for x in bag[1:]:
            if x != first:
                bag_without_first.append(x)
        new_set = bag_to_set(bag_without_first)
        if first not in new_set:
            new_set = [first] + new_set

    return new_set


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    """    
    smallest = 0
    largest = 0
    total = 0
    average = 0

    if len(values) == 1:
        smallest = values[0]
        largest = values[0]
        total = values[0]
        average = values[0]
    else:
        smallest, largest, total, average = list_stats(values[1:])
        if values[0] < smallest:
            smallest = values[0]
        if values[0] > largest:
            largest = values[0]
        total += values[0]
        average = total / len(values)
    return smallest, largest, total, average
    """
    smallest = values[0]
    largest = values[0]

    total = 0

    for value in values:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
        total += value

    average = total / len(values)

    return smallest, largest, total, average

