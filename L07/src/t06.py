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

values = input("Enter values for list seperated by spaces: ").split()

for i in values:
    lst.append(int(i))

print("List elements:", end=" ")
for value in lst:
    print(value, end=" ")

lst.reverse_r()

print()
print("Reversed list elements:", end=" ")
for value in lst:
    print(value, end=" ")

