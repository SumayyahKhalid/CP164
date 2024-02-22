'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = '2023-01-23'
'''

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    new_value = []
    for i in values:
        if i not in new_value:
            new_value.append(i)
    print(f"Cleaned:{new_value}")
    
    return None

def list_subtraction(minuend, subtrahend): 
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    a = 0
    temp = minuend.copy()
    for i in range(len(minuend)):
        if temp[i] == subtrahend[0]:
            minuend.pop(i-a)
            a += 1
    return None
    

def dsmvwl(string):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(string)
    -------------------------------------------------------
    Parameters:
       string - a string (str)
    Returns:
       out - string with the vowels removed (str)
    -------------------------------------------------------
    """
    out = ""
    VOWELS = ["a","e","i","o","u","A","E","I","O","U"]
    for i in string:
        if i not in VOWELS:
            out += i
    return out
    

def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged:
    Do not strip() the lines.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    upp, low, dig, whi, rem = 0, 0, 0, 0, 0
    for i in fv.read():
        if i.isupper():
            upp += 1
        elif i.islower():
            low += 1
        elif i.isdigit():
            dig += 1
        elif i == " ":
            whi += 1
        else:
            rem += 1
    return upp,low,dig,whi,rem


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    if year % 4 == 0:
        leap_year = True
        if year % 100 == 0:
            leap_year = False 
            if year % 400 == 0:
                leap_year = True 
            else:
                leap_year = False 
        else:
            leap_year = True 
    else:
        leap_year = False 
    return leap_year
    

def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = (name[0].isalpha() or name[0] == "-") and all (c.isalnum() or c == "_" for c in name)
    
    return valid
    

def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    if len(a) > 1:
        md = abs(a[1] - a[0])
        for i in range(1, len(a) - 1):
            diff = abs(a[i + 1] - a[i])
            if diff > md:
                md = diff
    else:
        md = 0
    return md


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = a[0][0]
    large = a[0][0]
    total = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] < small:
                small = a[i][j]
            if a[i][j] > large:
                large = a[i][j]
            total+=a[i][j]
    average = total/(len(a)*len(a[0]))
    return small,large,total,average


def matrixes_add(a, b):
    """
    -------------------------------------------------------
    Sums the contents of matrixes a and b. a and b must have
    the same number of rows and columns.
    a and b must be unchanged.
    Use: c = matrixes_add(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix sum of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    c = a
    for i in range(len(a)):
        for j in range(len(a[0])):
            c[i][j] = (a[i][j]+b[i][j])
    return c