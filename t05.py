'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jan. 11, 2024
'''

from Food_utilities import read_foods

fv = open("Foods.txt", "r")

foods = read_foods(fv)

for i in foods:
    print(i.__str__())
    print("------------------------------")