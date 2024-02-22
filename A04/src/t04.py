'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 9, 2023
'''

# Imports
from Queue_array import Queue

# Constants

target1 = Queue()
target2 = Queue()
source = Queue()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in arr:
    source.insert(i)

print("source")
for i in source:
    print(i)

print('')

target1, target2 = source.split_alt()

print("target1")
for i in target1:
    print(i)

print('')
print("target2")
for i in target2:
    print(i)

