'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jan. 11, 2024
'''

from Food import Food
from Food_utilities import write_foods

fv = open("foods.txt", "w")

k = Food("Biryani", 2, False, 130)
y = Food("Beaver Tail", 0, True, 500)

l = [k, y]

write_foods(fv, l)