# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:52:27 2022

@author: jense
"""
# Won't run    -5
a = [['Col 1', 'Col 2', 'Col 3', 'Col 4'], ['Row 1', 'Row 2', 'Row 3', 'Row 4']]

def display_table():
    print()
    for row in a:
        for item in row:
            print(item, end='  ')
        print()
        
values = [list(range(90, 100)), 
          list(range(100, 110)), 
          list(range(110, 120)), 
          list(range(120, 130)), 
          list(range(130, 140)), 
          list(range(140, 150)), 
          list(range(150, 160)), 
          list(range(160, 170)), 
          list(range(170, 180)), 
          list(range(180, 190)), 
          list(range(190, 200))]

display_table(values)


# solution

def display_table(twoD_list, column_width):
    # Note: you can use a variable for the field width by enclosing it in braces
    
    # indent headers by width of max row index 
    indent = len(str(len(twoD_list)))
    print(f'{"":{indent}}', end='')

    for col in range(len(twoD_list[0])):
        print(f'{col:>{column_width}}', end='')

    print()

    for i, row in enumerate(twoD_list):
        print(f'{i:>{indent}}', end='')

        for value in row:
            print(f'{value:>{column_width}}', end='')

        print()
          
values = [list(range(90, 100)), 
          list(range(100, 110)), 
          list(range(110, 120)), 
          list(range(120, 130)), 
          list(range(130, 140)), 
          list(range(140, 150)), 
          list(range(150, 160)), 
          list(range(160, 170)), 
          list(range(170, 180)), 
          list(range(180, 190)), 
          list(range(190, 200))]

display_table(values, 5)