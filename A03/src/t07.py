'''
Author: Sumayyah Khalid
ID: 169022335
Email: khal2335@mylaurier.ca
__updated__:Jun. 2, 2023
'''

from functions import stack_maze
def main():
    maze = {'Start': ['A'], 'A':['C', 'B'], 
            'B':[], 'C':['D', 'X']}
    path = stack_maze(maze)
    print(path)
main()