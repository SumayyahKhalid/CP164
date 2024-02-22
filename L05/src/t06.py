'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 14, 2023
'''


# Imports
from functions import bag_to_set
# Constants

bag = input("Enter a list of values (separated by commas): ").split(',')
new_set = bag_to_set(bag)
new_set = list(map(int, new_set))
print("Final set:", new_set)