'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 28, 2023
'''

# Imports
from List_linked import List
from Sorts_List_linked import Sorts
# Constants

arr = [12, 43, 65, 98, 57, 4, 8, 25, 33, 41]

lst = List()

for val in arr:
    lst.append(val)

print("List before radix sort: ")
for i in lst:
    print(i)

Sorts.radix_sort(lst)

print("\nList after radix sort: ")
for i in lst:
    print(i)
