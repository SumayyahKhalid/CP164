'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jan. 29, 2023
'''

from Food_utilities import food_table
from Food import Food
def main():
    food = Food("BBQ Pork",1,False,920)
    food1 = Food("Beef with Green Pepper",1,False,251)
    foods = [food1,food]
    food_table(foods)
    #print(food1.name)
main()