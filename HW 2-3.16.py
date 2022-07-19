# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 20:06:36 2022

@author: jense
"""

#this was hard and i wouldnt know how to do this without solution notes
#range 2-10 works but so does range 8 which doesnt make sense, should be 9

largest = int(input('Enter number: '))
number = int(input('Enter number: '))

if number > largest:
    next_largest = largest
    largest = number
else:
    next_largest = number

for counter in range(8):
    number = int(input('Enter number: '))

    if number > largest:
        next_largest = largest
        largest = number
    elif number > next_largest:
        next_largest = number

print(f'The largest number is {largest}')
print(f'The second largest number is {next_largest}')
