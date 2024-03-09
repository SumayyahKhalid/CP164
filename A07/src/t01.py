'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jul. 7, 2023
'''

# Imports
from List_linked import List

# Constants

food_list = List()


food_list.append('Lasagna|7|False|135')
food_list.append('Butter Chicken|2|False|490')
food_list.append('Moo Goo Guy Pan|1|False|272')
food_list.append('Vegetable Alicha|3|True|138')
food_list.append('Spanakopita|5|True|260')

# __eq__
print("--__eq__--")
food1 = food_list[0]
food2 = food_list[1]

equal = food1.__eq__(food2)
print(equal)

print(" ")

# __getitem__
print("--__getitem__--")
print(food_list[3])

print(" ")

# append
print("--append--")
new_food = "25"
food_list.append(new_food)
for i in food_list:
    print(i)

print(" ")

# clean
print("--clean--")
food_list = List()

food_list.append('Lasagna|7|False|135')
food_list.append('Butter Chicken|2|False|490')
food_list.append('Moo Goo Guy Pan|1|False|272')
food_list.append('Vegetable Alicha|3|True|138')
food_list.append('Spanakopita|5|True|260')
food_list.append('Spanakopita|5|True|260')
food_list.append('Spanakopita|5|True|260')
food_list.append('Spanakopita|5|True|260')
food_list.append('Spanakopita|5|True|260')
food_list.append('Spanakopita|5|True|260')
food_list.append('Spanakopita|5|True|260')
food_list.append('Spanakopita|5|True|260')

food_list.clean()
for i in food_list:
    print(i)

print(" ")

# combine
print("--combine--")
food_list1 = List()


food_list1.append('Lasagna|7|False|135')
food_list1.append('Butter Chicken|2|False|490')
food_list1.append('Moo Goo Guy Pan|1|False|272')
food_list1.append('Vegetable Alicha|3|True|138')
food_list1.append('Spanakopita|5|True|260')

food_list2 = List()

food_list2.append('Chirashi Don|6|False|600')
food_list2.append('Canuck Burger|0|False|7500')
food_list2.append('Turducken|8|False|12240')
food_list2.append('Shark Fin Soup|1|False|46')
food_list2.append('Chamuco|4|True|150')

target = List()

target.combine(food_list1, food_list2)

for i in target:
    print(i)

print(" ")

# intersection
print("--intersection--")
food_list1 = List()


food_list1.append('Lasagna|7|False|135')
food_list1.append('Butter Chicken|2|False|490')
food_list1.append('Moo Goo Guy Pan|1|False|272')
food_list1.append('Vegetable Alicha|3|True|138')
food_list1.append('Spanakopita|5|True|260')

food_list2 = List()


food_list2.append('Chirashi Don|6|False|600')
food_list2.append('Canuck Burger|0|False|7500')
food_list2.append('Turducken|8|False|12240')
food_list2.append('Shark Fin Soup|1|False|46')
food_list2.append('Chamuco|4|True|150')

target = List()

target.intersection(food_list1, food_list2)

for i in target:
    print(i)

print(" ")

# remove front
print("--remove_front--")
food_list = List()


food_list.append('Lasagna|7|False|135')
food_list.append('Butter Chicken|2|False|490')
food_list.append('Moo Goo Guy Pan|1|False|272')
food_list.append('Vegetable Alicha|3|True|138')
food_list.append('Spanakopita|5|True|260')

print("Initial list")
for i in food_list:
    print(i)

food_list.remove_front()

print(" ")
print("After using remove_front")
for i in food_list:
    print(i)

print(" ")

# remove many
print("--remove_many--")
food_list = List()

food_list.append('Lasagna|7|False|135')
food_list.append('Butter Chicken|2|False|490')
food_list.append('Moo Goo Guy Pan|1|False|272')
food_list.append('Vegetable Alicha|3|True|138')
food_list.append('Spanakopita|5|True|260')

key1 = 'Spanakopita|5|True|260'
key2 = 'Vegetable Alicha|3|True|138'

food_list.remove_many(key1)
food_list.remove_many(key2)

for i in food_list:
    print(i)

print(" ")

# split
print("--split--")
food_list = List()

food_list.append('Lasagna|7|False|135')
food_list.append('Butter Chicken|2|False|490')
food_list.append('Moo Goo Guy Pan|1|False|272')
food_list.append('Vegetable Alicha|3|True|138')
food_list.append('Spanakopita|5|True|260')

target1 = List()
target2 = List()
target1, target2 = food_list.split()

print("Target 1:")
for i in target1:
    print(i)

print(" ")

print("Target 2:")
for i in target2:
    print(i)

print(" ")

# split_alt
print("--split_alt--")
food_list = List()

food_list.append('Lasagna|7|False|135')
food_list.append('Butter Chicken|2|False|490')
food_list.append('Moo Goo Guy Pan|1|False|272')
food_list.append('Vegetable Alicha|3|True|138')
food_list.append('Spanakopita|5|True|260')

target1 = List()
target2 = List()
target1, target2 = food_list.split_alt()

print("Target 1:")
for i in target1:
    print(i)

print(" ")

print("Target 2:")
for i in target2:
    print(i)

print(" ")

# union
print("--union--")
food_list1 = List()

food_list1.append('Lasagna|7|False|135')
food_list1.append('Butter Chicken|2|False|490')
food_list1.append('Moo Goo Guy Pan|1|False|272')
food_list1.append('Vegetable Alicha|3|True|138')
food_list1.append('Spanakopita|5|True|260')

food_list2 = List()

food_list2.append('Chirashi Don|6|False|600')
food_list2.append('Canuck Burger|0|False|7500')
food_list2.append('Turducken|8|False|12240')
food_list2.append('Shark Fin Soup|1|False|46')
food_list2.append('Chamuco|4|True|150')


target = List()

target.union(food_list1, food_list2)

for i in target:
    print(i)

