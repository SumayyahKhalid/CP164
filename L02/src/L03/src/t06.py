'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 1, 2023
'''

# Imports
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq
from utilities import pq_to_array
from utilities import priority_queue_test
from Food_utilities import read_foods

# opening movies text file for reading
fv = open("foods.txt", "r")

# putting it into function read_movies from lab 1
foods = read_foods(fv)

# closing the text file
fv.close()

pq = Priority_Queue()

priority_queue_test(foods)

print()

array_to_pq(pq, foods)

for i in pq:
    print(i)

target = []

pq_to_array(pq, target)

for values in target:
    print(values)
