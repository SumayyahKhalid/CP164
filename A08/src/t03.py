'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 14, 2023
'''

# Imports
from BST_linked import BST
from Letter import Letter
from functions import letter_table, insert_test, do_comparisons
# Constants

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
insert_test(bst1, DATA1)

fv = open("otoos610.txt", "r")
do_comparisons(fv, bst1)

letter_table(bst1)
fv.close()
