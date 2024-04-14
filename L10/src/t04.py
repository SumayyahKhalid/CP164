'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 20, 2023
'''

# Imports
from test_Sorts_List_linked import test_sort, SORTS, SIZE
# Constants

print("n:{:^10d}    |{:^24s}|\t|{:^22s}|".format(SIZE, "Comparisons", "Swaps"))
print("{:<15s} {:<8s} {:<8s} {:^8s}\t{:<8s} {:<8s} {:<8s}".format("Algorithm",
                                                                  "In Order", "Reversed",
                                                                  "Random", "In Order",
                                                                  "Reversed", "Random"))
SEP = "-"

for sort in SORTS:
    title = sort[0]
    sort_func = sort[1]
    test_sort(title, sort_func)

