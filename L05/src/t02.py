'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 14, 2023
'''

# Imports
from functions import gcd
# Constants

m = int(input("Enter an integer: "))
n = int(input("Enter another integer: "))

ans = gcd(m, n)

print("The GCD of", m, "and", n, "is:", ans)

