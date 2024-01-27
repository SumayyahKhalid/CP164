'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jan. 11, 2024
'''

from Food_utilities import get_vegetarian, read_foods

fv = open("foods.txt", "r")

foods = read_foods(fv)

v = get_vegetarian(foods)

for i in v:
    print(i.__str__())
    print("----------------------")