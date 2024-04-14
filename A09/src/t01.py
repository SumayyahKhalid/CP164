'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 21, 2023
'''

# Imports
from functions import comparison_total, insert_words
from Hash_Set_array import Hash_Set
# Constants

fv = open("otoos610.txt", "r")
hash_set = Hash_Set(20)
insert_words(fv, hash_set)

total, max_word = comparison_total(hash_set)

print("Using array-based list Hash_set")
print("")
print(f"Total Comparisons: {total:,}")
print(
    f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,}")

