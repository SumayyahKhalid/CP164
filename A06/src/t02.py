'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 30, 2023
'''

# Imports
from Priority_Queue_linked import Priority_Queue
# Constants

print("Both Priority Queues below will be used for most tests.")

print(" ")

Priority_Queue_1 = Priority_Queue()
Priority_Queue_2 = Priority_Queue()

input_1 = input(
    "Enter a value to insert into Priority Queue 1, separated by spaces: ").split()
for i in input_1:
    Priority_Queue_1.insert(int(i))

input_2 = input(
    "Enter a value to insert into Priority Queue 2, separated by spaces: ").split()
for i in input_2:
    Priority_Queue_2.insert(int(i))

print("")
print("--insert--")

print(" ")
print("Priority Queue 1:")
for i in Priority_Queue_1:
    print(i)

print(" ")
print("Priority Queue 2:")
for i in Priority_Queue_2:
    print(i)

print(" ")
print("--is_empty--")
empty = Priority_Queue_1.is_empty()
print("Priority Queue 1 is empty: {}".format(empty))

print(" ")
print('--remove--')
value = Priority_Queue_1.remove()

print("Priority Queue 1 after removing {}:".format(value))
for i in Priority_Queue_1:
    print(i)

print(" ")

print("--peek--")
value = Priority_Queue_1.peek()
print("Priority Queue 1 after peeking: {}".format(value))
for i in Priority_Queue_1:
    print(i)

print(" ")
print("--split_alt--")
target1 = Priority_Queue()
target2 = Priority_Queue()

target1, target2 = Priority_Queue_1.split_alt()

print("Target 1:")
for i in target1:
    print(i)

print(" ")
print("Target 2:")
for i in target2:
    print(i)

print(" ")
print("--split_key--")
target1 = Priority_Queue()
target2 = Priority_Queue()

key = int(input("Enter a key to split Priority Queue 1 by: "))

target1, target2 = Priority_Queue_1.split_key(key)

print("Target 1:")
for i in target1:
    print(i)

print(" ")
print("Target 2:")
for i in target2:
    print(i)

print(" ")
print("--combine--")
target = Priority_Queue()

target.combine(Priority_Queue_1, Priority_Queue_2)

print("Target after combine:")
for i in target:
    print(i)

print(" ")
print("--_append_queue--")
print("Using new Priority Queue 1 and Priority Queue 2:")
Priority_Queue_1 = Priority_Queue()
Priority_Queue_2 = Priority_Queue()

input_1 = input(
    "Enter a value to insert into Priority Queue 1, separated by spaces: ").split()
for i in input_1:
    Priority_Queue_1.insert(int(i))

input_2 = input(
    "Enter a value to insert into Priority Queue 2, separated by spaces: ").split()
for i in input_2:
    Priority_Queue_2.insert(int(i))
Priority_Queue_2._append_queue(Priority_Queue_1)
print(" ")
print("Priority Queue 2 after appending Priority Queue 1:")
for i in Priority_Queue_2:
    print(i)

print(" ")
print("--_move_front_to_rear--")
print("Using new Priority Queue 1 and Priority Queue 2:")
Priority_Queue_1 = Priority_Queue()
Priority_Queue_2 = Priority_Queue()

input_1 = input(
    "Enter a value to insert into Priority Queue 1, separated by spaces: ").split()
for i in input_1:
    Priority_Queue_1.insert(int(i))

input_2 = input(
    "Enter a value to insert into Priority Queue 2, separated by spaces: ").split()
for i in input_2:
    Priority_Queue_2.insert(int(i))
print(" ")
print("Priority Queue 1 before moving front to rear:")
for i in Priority_Queue_1:
    print(i)


Priority_Queue_1._move_front_to_rear(Priority_Queue_2)

print("Priority Queue 1 after moving front to rear:")
for i in Priority_Queue_1:
    print(i)

