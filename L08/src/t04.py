'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 6, 2023
'''

# Imports
from morse import ByCode, fill_code_bst
from BST_linked import BST
# Constants

a = ByCode('A', '.-')
b = ByCode('B', '-...')
c = ByCode('C', '-.-.')

bst = BST()

values = [(a.letter, a.code), (b.letter, b.code), (c.letter, c.code)]
fill_code_bst(bst, values)

v = bst.inorder()

for i in v:
    print(i)
