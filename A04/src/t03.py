'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 9, 2023
'''

# Imports
from functions import queue_split_alt
from Queue_circular import Queue

# Constants

test = Queue()
count = int(input("Number of values: "))
for i in range(count):
    value = int(input(f"Value {i+1}: "))
    test.insert(value)
target1, target2 = queue_split_alt(test)

print("Target 1: ")
for i in target1:
    print(i)
print()

print("Target 2: ")
for i in target2:
    print(i)
