'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Feb. 16, 2024
'''

from List_linked import List
l = List()
l.append(5)
l.append(99)
l.remove(99)
for v in l:
    print(v)
    
print(l[0])
l[0] = 66
print(l[0])