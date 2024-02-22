'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = '2023-01-23'
'''



from functions import file_analyze

fv = open("functions.py")
upp, low, dig, whi, rem = file_analyze(fv)
print(upp)
print(low)
print(dig)
print(whi)
print(rem)