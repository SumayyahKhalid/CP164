'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jan. 20, 2024
'''

from Food import Food
from Food_utilities import by_origin
def main():

    food = Food("grape",3,True,67)
    food1 = Food("chicken",2,False,67)
    food2 = Food("sushi",3,True,67)
    foods = [food,food1,food2]
    v = by_origin(foods,3)
    for s in v:
        print(s)
        
main()