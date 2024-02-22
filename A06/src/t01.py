'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 30, 2023
'''


# Imports
from Queue_linked import Queue
# Constants

queue = Queue()

print("Input queue below will be used to test all functions.")

values = input("Enter values to queue, separated by commas: ").split(",")

print(" ")
print("--insert--")
for value in values:
    queue.insert((value))

print("Queue after insert:")
for i in queue:
    print(i)

print(" ")

print("--is_empty--")
empty = queue.is_empty()
print("Empty: {}".format(empty))

print(" ")

print("--remove--")
value = queue.remove()

print("Queue after remove:")
for value in queue:
    print(value)

print(" ")

print("--peek--")
value = queue.peek()

print("Queue after peek:")
for value in queue:
    print(value)

print(" ")

print("--_move_front_to_rear--")
target = Queue()

target.insert(1)
target.insert(2)
target.insert(3)

print("Target queue before _move_front_to_rear:")
for value in target:
    print(value)

print(" ")

queue._move_front_to_rear(target)

print("Queue after _move_front_to_rear:")
for value in queue:
    print(value)

print(" ")

print("--_append_queue--")
target = input(
    "Enter values to append into queue-2, separated by commas: ").split(",")
queue2 = Queue()
for value in target:
    queue2.insert(value)

queue._append_queue(queue2)

print("Queue after _append_queue:")
for value in queue:
    print(value)

print(" ")

print("--combine--")
target = input(
    "Enter values to append into queue-2, separated by commas: ").split(",")
queue2 = Queue()
for value in target:
    queue2.insert(value)

final_queue = Queue()

final_queue.combine(queue, queue2)

print("Final queue after combine:")
for value in final_queue:
    print(value)

print(" ")

print("--split_alt--")
target2 = Queue()
target2.insert(1)
target2.insert(2)
target2.insert(3)
print("Target 2 before split_alt:")
for value in target2:
    print(value)

print(" ")
queue, target2 = queue.split_alt()

print("Target 1 after split_alt:")
for value in queue:
    print(value)

print(" ")

print("Target 2 after split_alt:")
for value in target2:
    print(value)

print(" ")

print("__eq__")
target = input(
    "Enter values to append into queue-2, separated by commas: ").split(",")
queue2 = Queue()
for value in target:
    queue2.insert(value)

equal = queue == queue2
print("Equal: {}".format(equal))

