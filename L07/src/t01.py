'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 29, 2023
'''

# Imports
from List_linked import List
# Constants

lst = List()

values = input("Enter a list of integers separated by spaces: ").split()

for i in values:
    lst.append(int(i))

print("List elements:", end=" ")
for value in lst:
    print(value, end=" ")

print()
key = int(input("Enter an integer key to search for: "))

previous, current, index = lst._linear_search_r(key)

if index == -1:
    print(f"The key {key} was not found in the list.")
else:
    print(f"The key {key} was found at index {index}.")

