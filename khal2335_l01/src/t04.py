'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jan. 11, 2024
'''

from Food import Food
from Food_utilities import read_food

k = read_food("Spanakopita|5|True|260")

print(k.__str__())

t = Food("blank", 5, True, 0)