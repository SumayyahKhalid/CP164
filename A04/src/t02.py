'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 9, 2023
'''


# Imports
from Queue_circular import Queue
from utilities import array_to_queue

# Constants

queue1, queue2, queue3 = Queue(), Queue(), Queue()
source1 = [4, 3, 2, 1, 0]
source2 = [0, 1, 2, 3, 4]
source3 = [3, 2, 1, 0, 4]

array_to_queue(queue1, source1)
array_to_queue(queue2, source2)
array_to_queue(queue3, source3)

print("Results: ")
print("")
print(f"{list(queue1)} == {list(queue2)}: {queue1 == queue2}")
print(f"{list(queue2)} == {list(queue3)}: {queue1 == queue3}")

