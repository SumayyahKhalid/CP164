'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 2, 2023
'''

# Imports
from Stack_array import Stack

# Constants
OPERATORS = "+-*/"
NUMBERS = "12356890"


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()

    while not source1.is_empty() and not source2.is_empty():
        target.push(source1.pop())
        target.push(source2.pop())

    while not source1.is_empty():
        target.push(source1.pop())

    while not source2.is_empty():
        target.push(source2.pop())

    return target
    
    
def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    temp_stack = Stack()

    while not source.is_empty():
        temp_stack.push(source.pop())

    while not temp_stack.is_empty():
        source.push(temp_stack.pop())

    return


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    chars = ""
    for s in string:
        if s.isalpha():
            chars += s.lower()
            
    l = len(chars)
    mid = -1
    if l == 0:
        palindrome = True
    else:
        mid = l // 2
        first_half = Stack()
        for i in range(mid):
            first_half.push(chars[i])
        if l % 2 == 0:
            second_half_chars = chars[mid:]
        else:
            second_half_chars = chars[mid + 1:]
        second_half_chars = second_half_chars.lower()  
        i = 0
        while palindrome and i < mid:
            s = second_half_chars[i]
            p = first_half.pop()
            if s == p:
                i += 1
            else:
                palindrome = False
    return palindrome



def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()

    for char in string.split():
        if char.isdigit():
            stack.push(int(char))
        elif char in OPERATORS:
            sign2 = stack.pop()
            sign1 = stack.pop()
            if char == '+':
                result = sign1 + sign2
            elif char == '-':
                result = sign1 - sign2
            elif char == '*':
                result = sign1 * sign2
            else:
                result = sign1 / sign2
            stack.push(result)
    answer = stack.pop()

    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    try:
        current = "Start"
        choices = maze[current]
        path = []
        if "X" in choices:
            path.append("X")
        stack = Stack()
        while "X" not in choices:
            for c in choices:
                stack.push(c)
            current = stack.pop()
            if maze[current]!=[]:
                path.append(current)          
            choices = maze[current]
            if "X" in choices:
                path.append("X")
    except:     
        path = None
    finally:
        return path
