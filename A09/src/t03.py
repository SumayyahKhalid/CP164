'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 21, 2023
'''

# Imports
from functions import comparison_total, insert_words
from Hash_Set_BST import Hash_Set
# Constants

fv = open("otoos610.txt", "r")
hs = Hash_Set(20)
insert_words(fv, hs)

total, max_word = comparison_total(hs)

print("Using linked BST Hash_set")
print("")
print(f"Total Comparisons: {total:,}")
print(
    f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,}")

