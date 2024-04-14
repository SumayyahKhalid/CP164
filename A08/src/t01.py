'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 14, 2023
'''

# Imports
from BST_linked import BST
# Constants

print("--__eq__--")
bst = BST()

for val in [11, 24, 67, 25, 73, 13]:
    bst.insert(val)

print("BST 1 contents: ")
for i in bst:
    print(i)

bst2 = BST()

for val in [12, 1, 36, 54, 24]:
    bst2.insert(val)

print("BST 2 contents: ")
for k in bst2:
    print(k)

print(" ")

print("Are both BSTs equal? ", bst == bst2)

print(" ")
print("--is_balanced--")
b = bst.is_balanced()
print("Is BST balanced? ", b)

print(" ")
print("--is_valid--")
b = bst.is_valid()
print("Is BST valid? ", b)

print(" ")
print("--min--")
value = bst.min()
print("Min value in BST: ", value)

print(" ")
print("--leaf_count--")
count = bst.leaf_count()
print("Number of leaves in BST: ", count)

print(" ")
print("--one_child_count--")
count = bst.one_child_count()
print("One child count: ", count)

print(" ")
print("--two_child_count--")
count = bst.two_child_count()
print("Two child count: ", count)

print(" ")
print("--inorder--")
print("Inorder traversal: ")
for i in bst.inorder():
    print(i)

print(" ")
print("--preorder--")
print("Preorder traversal: ")
for i in bst.preorder():
    print(i)

print(" ")
print("--postorder--")
print("Postorder traversal: ")
for i in bst.postorder():
    print(i)

print(" ")
print("--remove--")
key = 11
print("Key: ", key)
bst.remove(key)
print("BST after removing: ")
for i in bst:
    print(i)

