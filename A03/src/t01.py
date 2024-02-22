'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 2, 2023
'''

# Imports
from Stack_array import Stack
from functions import stack_combine

# Constants

source1 = Stack()
source1.push(1)
source1.push(3)
source1.push(5)

source2 = Stack()
source2.push(2)
source2.push(4)
source2.push(6)


target = stack_combine(source1, source2)
num_columns = 3
values = []

while not target.is_empty():
    values.append(target.pop())

num_rows = (len(values) + num_columns - 1) // num_columns

for row in range(num_rows):
    for col in range(num_columns):
        index = row + col * num_rows
        if index < len(values):
            print(f"{values[index]:<5}", end="")
    print()
