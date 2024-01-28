'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 1, 2023
'''

# Imports
from utilities import array_to_queue
from utilities import queue_to_array
from utilities import queue_test
from Queue_array import Queue
# Constants

source_input = input("Enter elements separated by commas: ")
source = source_input.split(',')
source = [int(i) for i in source]

queue = Queue()
array_to_queue(queue, source)

for i in queue:
    print(i)

print()

target = []

queue = Queue()

queue.insert(1)
queue.insert(2)
queue.insert(3)

queue_to_array(queue, target)

print(target)

print()

source_input = input("Enter elements separated by commas for testing: ")
source = source_input.split(',')
source = [int(i) for i in source]

queue = Queue()

print("\nQueue Test:")

queue_test(source)
queue = list(map(int, queue))
print("Queue: ", queue)
