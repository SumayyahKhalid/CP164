'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 14, 2023
'''

# Imports
from functions import recurse
# Constants

x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))

ans = recurse(x, y)

print("Final result:", ans)
