# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:52:27 2022

@author: jense
"""

a = [['Col 1', 'Col 2', 'Col 3', 'Col 4'], ['Row 1', 'Row 2', 'Row 3', 'Row 4']]

def display_table():
    print()
    for row in a:
        for item in row:
            print(item, end='  ')
        print()