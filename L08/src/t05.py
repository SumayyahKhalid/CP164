'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 6, 2023
'''

# Imports
from morse import ByLetter, encode_morse, fill_letter_bst
from BST_linked import BST
# Constants

a = ByLetter('A', '.-')
b = ByLetter('B', '-...')
c = ByLetter('C', '-.-.')

bst = BST()
values = [(a.letter, a.code), (b.letter, b.code), (c.letter, c.code)]
fill_letter_bst(bst, values)
bst.inorder()
text = "ABC"
result = encode_morse(bst, text)

print(result)
