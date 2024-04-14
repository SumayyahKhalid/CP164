'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 13, 2023
'''

# Imports
from Hash_Set_array import Hash_Set
# Constants

print("Testing insert:")
hset = Hash_Set(1)
hset.insert(2)
hset.insert(3)
hset.insert(4)
hset.insert(5)

print("Hash set after inserting: ")
for i in hset:
    print(i)

print(" ")

print("Testing remove:")

removed = hset.remove(3)

print("Removed value: ", removed)

print("Hash set after removing: ")
for i in hset:
    print(i)

