# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:48:58 2022

@author: jense
"""


letter_tuple = ()
letter_tuple = 'a', 'x', 'h', 'b', 'r', 'v', 'b', 'g', 'r', 'v', 'j', 'c', 'b'



def summarize_letters(str):
    letters: []
    count: []
    
summary = summarize_letters(str())



for char, count in summary:
    # WOn't run becuase of object type   -5
    print(f'{char} appears {count} times in letters')        
        
        
key = 'abcdefghijklmnopqrstuvwxyz'
if key in letter_tuple:
    print(f'found {key} at index {letter_tuple.index(key)}')
else:
    print(f'{key} not found')