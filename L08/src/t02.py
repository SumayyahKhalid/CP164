'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 6, 2023
'''

# Imports
from morse import ByCode
# Constants

print("Testing ByCode class.")
print(" ")

letter1 = input("Enter the first letter: ")
code1 = input("Enter the morse code for the first letter: ")

print(" ")

letter2 = input("Enter the second letter: ")
code2 = input("Enter the morse code for the second letter: ")

bl1 = ByCode(letter1.upper(), code1)
bl2 = ByCode(letter2.upper(), code2)

print(" ")

print("ByCode object 1: ", bl1)
print("ByCode object 2: ", bl2)

print(" ")
print("--__eq__--")
print("Are both ByCode objects equal? {}".format(bl1 == bl2))

print(" ")
print("--__lt__--")
print("Does ByCode object 1 come before ByCode object 2? {}".format(bl1 < bl2))
print("Does ByCode object 2 come before ByCode object 1? {}".format(bl2 < bl1))

print(" ")
print("--__le__--")
print("Is ByCode object 1 equal to or preceeding ByCode object 2? {}".format(bl1 <= bl2))
print("Is ByCode object 2 equal to or preceeding ByCode object 1? {}".format(bl2 <= bl1))

print(" ")
print("--__str__--")
print("Formatted string of ByCode object 1: {}".format(str(bl1)))
print("Formatted string of ByCode object 2: {}".format(str(bl2)))

