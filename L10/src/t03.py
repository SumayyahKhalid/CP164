'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 20, 2023
'''

# Imports
from test_Sorts_List_linked import create_randoms, create_reversed, create_sorted
# Constants

sorted_list = create_sorted()
reversed_list = create_reversed()
random_list = create_randoms()

print("Sorted:")
for num in sorted_list:
    print(num)

print("Reversed:")
for num in reversed_list:
    print(num)

print("Random Lists:")
print("[", end="")
for i in random_list:
    print("[", end="")
    for k in i:
        print(k, end=", ")
    print("]", end="")

