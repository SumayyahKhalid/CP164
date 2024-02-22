'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 2, 2023
'''

# Imports
from Stack_array import Stack

# Constants

s1 = Stack()
s2 = Stack()

for i in range(5):
    s1.push(i)
    s2.push(i + 10)
print("stack 1:")
for i in s1:
    print(i)

print()
print("stack 2:")
for i in s2:
    print(i)

print()
print("target:")
target = Stack()
target.combine(s1, s2)
for i in target:
    print(i)