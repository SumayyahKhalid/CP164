'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 6, 2023
'''

# Imports
from morse import ByLetter
# Constants

print("Testing ByLetter class.")
print(" ")

letter1 = input("Enter the first letter: ")
code1 = input("Enter the morse code for the first letter: ")

print(" ")

letter2 = input("Enter the second letter: ")
code2 = input("Enter the morse code for the second letter: ")

bl1 = ByLetter(letter1.upper(), code1)
bl2 = ByLetter(letter2.upper(), code2)

print(" ")

print("ByLetter object 1: ", bl1)
print("ByLetter object 2: ", bl2)

print(" ")
print("--__eq__--")
print("Are both ByLetter objects equal? {}".format(bl1 == bl2))

print(" ")
print("--__lt__--")
print("Does ByLetter object 1 come before ByLetter object 2? {}".format(bl1 < bl2))
print("Does ByLetter object 2 come before ByLetter object 1? {}".format(bl2 < bl1))

print(" ")
print("--__le__--")
print("Is ByLetter object 1 equal to or preceeding ByLetter object 2? {}".format(bl1 <= bl2))
print("Is ByLetter object 2 equal to or preceeding ByLetter object 1? {}".format(bl2 <= bl1))

print(" ")
print("--__str__--")
print("Formatted string of ByLetter object 1: {}".format(str(bl1)))
print("Formatted string of ByLetter object 2: {}".format(str(bl2)))