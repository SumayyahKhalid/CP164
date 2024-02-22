'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 2, 2023
'''

# Imports
from functions import stack_reverse
from Stack_array import Stack

# Constants

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack_reverse(stack)

for i in stack:
    print(i)
