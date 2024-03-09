'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 7, 2023
'''

# Imports
from Sorted_List_linked import Sorted_List

# Constants

food_list = Sorted_List()

food_list.insert('Lasagna|7|False|135')
food_list.insert('Butter Chicken|2|False|490')
food_list.insert('Moo Goo Guy Pan|1|False|272')
food_list.insert('Vegetable Alicha|3|True|138')
food_list.insert('Spanakopita|5|True|260')

# insert
print("--insert--")
print("Food list after inserting objects: ")
for i in food_list:
    print(i)

print(" ")

# __eq__
print("--__eq__--")
food1 = food_list[0]
food2 = food_list[1]

equal = food_list[0] == food_list[1]
print(equal)

print(" ")

# getitem
print("--getitem--")
print(food_list[3])

print(" ")

# clean
print("--clean--")
food_list = Sorted_List()
food_list.insert('Lasagna|7|False|135')
food_list.insert('Butter Chicken|2|False|490')
food_list.insert('Moo Goo Guy Pan|1|False|272')
food_list.insert('Vegetable Alicha|3|True|138')
food_list.insert('Spanakopita|5|True|260')

food_list.clean()
for i in food_list:
    print(i)

print(" ")

# intersection
print("--intersection--")
food_list1 = Sorted_List()
food_list2 = Sorted_List()

target = Sorted_List()

food_list1.insert('Lasagna|7|False|135')
food_list1.insert('Butter Chicken|2|False|490')
food_list1.insert('Moo Goo Guy Pan|1|False|272')

food_list2.insert("Vegetable Alicha|3|True|138")
food_list2.insert("Spanakopita|5|True|260")
food_list2.insert('Chirashi Don|6|False|600')

target.intersection(food_list1, food_list2)

for i in target:
    print(i)

print(" ")

# union
print("--union--")
food_list1 = Sorted_List()
food_list2 = Sorted_List()

target = Sorted_List()

food_list1.insert('Lasagna|7|False|135')
food_list1.insert('Butter Chicken|2|False|490')
food_list1.insert('Moo Goo Guy Pan|1|False|272')

food_list2.insert("Vegetable Alicha|3|True|138")
food_list2.insert("Spanakopita|5|True|260")
food_list2.insert('Chirashi Don|6|False|600')

target.union(food_list1, food_list2)

for i in target:
    print(i)

print(" ")

# __contains__
print("--__contains__--")
food_list1 = Sorted_List()

food_list1.insert('Lasagna|7|False|135')
food_list1.insert('Butter Chicken|2|False|490')
food_list1.insert('Moo Goo Guy Pan|1|False|272')
food_list1.insert('Vegetable Alicha|3|True|138')
food_list1.insert('Spanakopita|5|True|260')

key = 'Lasagna|7|False|135'

print(key in food_list1)

print(" ")

# remove_front
print("--remove_front--")
food_list = Sorted_List()

food_list.insert('Lasagna|7|False|135')
food_list.insert('Butter Chicken|2|False|490')
food_list.insert('Moo Goo Guy Pan|1|False|272')
food_list.insert('Vegetable Alicha|3|True|138')
food_list.insert('Spanakopita|5|True|260')

food_list.remove_front()
for i in food_list:
    print(i)

print(" ")

# remove
print("--remove--")
food_list = Sorted_List()

food_list.insert('Lasagna|7|False|135')
food_list.insert('Butter Chicken|2|False|490')
food_list.insert('Moo Goo Guy Pan|1|False|272')
food_list.insert('Vegetable Alicha|3|True|138')
food_list.insert('Spanakopita|5|True|260')

key = "Spanakopita|5|True|260"

value = food_list.remove(key)

print("Removed object: ", value)

print(" ")

# count
print("--count--")
food_list1 = Sorted_List()


food_list1.insert('Lasagna|7|False|135')
food_list1.insert('Butter Chicken|2|False|490')
food_list1.insert('Moo Goo Guy Pan|1|False|272')
food_list1.insert('Vegetable Alicha|3|True|138')
food_list1.insert('Spanakopita|5|True|260')

key = 'Lasagna|7|False|135'

print(food_list1.count(key))

print(" ")

# find
print("--find--")
food_list1 = Sorted_List()

food_list1.insert('Lasagna|7|False|135')
food_list1.insert('Butter Chicken|2|False|490')
food_list1.insert('Moo Goo Guy Pan|1|False|272')
food_list1.insert('Vegetable Alicha|3|True|138')
food_list1.insert('Spanakopita|5|True|260')

key = '|False|490'

value = food_list1.find(key)

print(value)

print(" ")

# index
print("--index--")
food_list1 = Sorted_List()

food_list1.insert('Lasagna|7|False|135')
food_list1.insert('Butter Chicken|2|False|490')
food_list1.insert('Moo Goo Guy Pan|1|False|272')
food_list1.insert('Vegetable Alicha|3|True|138')
food_list1.insert('Spanakopita|5|True|260')

key = 'Moo Goo Guy Pan|1|False|272'

n = food_list1.index(key)

print(n)

print(" ")

# max
print("--max--")
food_list1 = Sorted_List()

food_list1.insert('Lasagna|7|False|135')
food_list1.insert('Butter Chicken|2|False|490')
food_list1.insert('Moo Goo Guy Pan|1|False|272')
food_list1.insert('Vegetable Alicha|3|True|138')
food_list1.insert('Spanakopita|5|True|260')

value = food_list1.max()

print(value)

print(" ")

# max
print("--min--")
food_list1 = Sorted_List()

food_list1.insert('Lasagna|7|False|135')
food_list1.insert('Butter Chicken|2|False|490')
food_list1.insert('Moo Goo Guy Pan|1|False|272')
food_list1.insert('Vegetable Alicha|3|True|138')
food_list1.insert('Spanakopita|5|True|260')

value = food_list1.min()

print(value)

print(" ")

# peek
print("--peek--")
food_list1 = Sorted_List()

food_list1.insert('Lasagna|7|False|135')
food_list1.insert('Butter Chicken|2|False|490')
food_list1.insert('Moo Goo Guy Pan|1|False|272')
food_list1.insert('Vegetable Alicha|3|True|138')
food_list1.insert('Spanakopita|5|True|260')

value = food_list1.peek()

print(value)

print(" ")

# remove
print("--remove--")
food_list1 = Sorted_List()

food_list1.insert('Lasagna|7|False|135')
food_list1.insert('Butter Chicken|2|False|490')
food_list1.insert('Moo Goo Guy Pan|1|False|272')
food_list1.insert('Vegetable Alicha|3|True|138')
food_list1.insert('Spanakopita|5|True|260')

key = 'Spanakopita|5|True|260'

value = food_list1.remove(key)

print(value)

print(" ")
print("List after removing:")
for i in food_list1:
    print(i)

print(" ")

# _linear_search
print("--_linear_search--")
food_list1 = Sorted_List()

food_list1.insert('Lasagna|7|False|135')
food_list1.insert('Butter Chicken|2|False|490')
food_list1.insert('Moo Goo Guy Pan|1|False|272')
food_list1.insert('Vegetable Alicha|3|True|138')
food_list1.insert('Spanakopita|5|True|260')

print("Food List: ")
for i in food_list1:
    print(i)

print(" ")

key = 'Vegetable Alicha|3|True|138'

print("Key: ", key)

i = food_list1._linear_search(key)

print("Search object: ", i)

