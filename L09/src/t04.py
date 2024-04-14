'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 13, 2023
'''

# Imports
from Hash_Set_array import Hash_Set
# Constants

hset = Hash_Set(5)
for i in range(8):
    hset.insert(i)

print("Before rehashing:")
hset.debug()

hset._rehash()

print("\nAfter rehashing:")
hset.debug()

