'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jan. 29, 2023
'''


from Food import Food
from Food_utilities import calories_by_origin

def main():
    food = Food("grape",3,True,5)
    food1 = Food("chicken",2,False,67)
    food2 = Food("sushi",3,True,12)
    food3 = Food("water",3,True,0)
    foods = [food,food1,food2,food3]
    a = calories_by_origin(foods, 3)
    print(a)
    
main()