'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__ = '2023-01-23'
'''

from functions import matrix_stats

a = [[2,-3,-1], [-5,-1,-7], [-3,-10,2], [-3,4,-9]]
small, large, total, average = matrix_stats(a)
print(f"{a}")
print(f"Smallest = {small}")
print(f"Largest = {large}")
print(f"Total = {total}")
print(f"Average = {average:.2f}")