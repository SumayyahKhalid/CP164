'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Feb. 2, 2024
'''

# Imports
from List_array import List
from Food_utilities import read_foods
from utilities import list_test
# Constants

fv = open("foods.txt", "r")

foods = read_foods(fv)

fv.close()

lst = List()

list_test(foods)
