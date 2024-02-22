'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 30, 2023
'''

# Imports
from Deque_linked import Deque
# Constants

Deque_init = Deque()


input_1 = input(
    "Enter a value to insert into initial Deque, separated by spaces. This will be used for most tests: ").split()
for i in input_1:
    Deque_init.insert_front(int(i))

print("Initial Deque:")
for i in Deque_init:
    print(i)

print(" ")

Deque1 = Deque()
print("--insert_front--")
input_deque1 = input(
    "Enter a value to insert into Deque1, separated by spaces: ").split()
for i in input_deque1:
    Deque1.insert_front(int(i))

print("Deque1:")
for i in Deque1:
    print(i)

print(" ")
Deque2 = Deque()
print("--insert_rear--")
input_deque2 = input(
    "Enter a value to insert into Deque2, separated by spaces: ").split()
for i in input_deque2:
    Deque2.insert_rear(int(i))

print("Deque2:")
for i in Deque2:
    print(i)

print(" ")
print("--is_empty--")
b = Deque_init.is_empty()
print("Initial Deque is empty: {}".format(b))

print(" ")
print("--remove_front--")
v = Deque_init.remove_front()
print("Removing front value: {}".format(v))
print("Initial Deque after remove_front:")
for i in Deque_init:
    print(i)

print(" ")
print("--remove_rear--")
v = Deque_init.remove_rear()
print("Removing rear value: {}".format(v))
print("Initial Deque after remove_rear:")
for i in Deque_init:
    print(i)

print(" ")
print("--peek_front--")
v = Deque_init.peek_front()
print("Peeking front value: {}".format(v))
print("Initial Deque after peek_front:")
for i in Deque_init:
    print(i)

print(" ")

print("--peek_rear--")
v = Deque_init.peek_rear()
print("Peeking rear value: {}".format(v))
print("Initial Deque after peek_rear:")
for i in Deque_init:
    print(i)

print(" ")
print("--_swap--")
node1 = Deque_init._front._next  # type: ignore
node2 = Deque_init._rear._prev  # type: ignore

Deque_init._swap(node1, node2)

print("Initial Deque after _swap:")
for i in Deque_init:
    print(i)


