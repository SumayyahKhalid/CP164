'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 20, 2023
'''

# Imports
from test_Sorts_array import create_randoms, create_reversed, create_sorted
# Constants

sorted_array = create_sorted()
reversed_array = create_reversed()
random_arrays = create_randoms()

print("Sorted:")
for num in sorted_array:
    print(num)

print("Reversed:")
for num in reversed_array:
    print(num)

print("Random Lists:")
print("[", end="")
for i in random_arrays:
    print("[", end="")
    for k in i:
        print(k, end=", ")
    print("]", end="")
