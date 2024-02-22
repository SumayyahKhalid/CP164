'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 9, 2023
'''

# Imports
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

# Constants

n = int(input("How many values do you want to insert into the source priority queue?: "))

source = Priority_Queue()

for i in range(n):
    value = int(input(f"Enter value for source priority queue {i + 1}: "))
    source.insert(value)

key = int(input("Enter the key to split the source priority queue: "))

target1, target2 = pq_split_key(source, key)

print(" ")

print("Values in target1:")
while not target1.is_empty():
    print(target1.remove())

print(" ")

print("Values in target2:")
while not target2.is_empty():
    print(target2.remove())

