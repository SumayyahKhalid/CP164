'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 29, 2023
'''


# Imports
from List_linked import List
# Constants

source1 = List()
source2 = List()
target = List()

source1_values = input("Enter values for source 1 seperated by spaces: ").split()

for i in source1_values:
    source1.append(int(i))

print("Source 1 elements:", end=" ")
for value in source1:
    print(value, end=" ")

print()

source2_values = input("Enter values for source 2 seperated by spaces: ").split()

for i in source2_values:
    source2.append(int(i))

print("Source 2 elements:", end=" ")
for value in source2:
    print(value, end=" ")

print()

target.intersection_r(source1, source2)

print("Target elements:", end=" ")
for value in target:
    print(value, end=" ")

