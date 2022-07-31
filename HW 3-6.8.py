# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 22:19:09 2022

@author: jense
"""

numberdict = {1: 'one', 3: 'three', 12: 'twelve', 43: 'fourty-three', 100: \
              'one hundred'}
    
amount = input('Enter a dollar amount less than 1000.00: ')
dollars, cents = amount.split('.')
# Either prompt for cents or perform error checking   -2
dollars = int(dollars)
cents = int(cents)
amount_in_words = []

if dollars == 0:
    amount_in_words.append(numberdict[dollars])
elif dollars >= 100:
    amount_in_words.append(numberdict[dollars // 100] + ' hundred')

dollars %= 100 

if dollars in range(10, 20):
    amount_in_words.append(numberdict[dollars])
elif dollars in range(20, 100):
    amount_in_words.append(numberdict[dollars // 10 * 10])
    dollars %= 10 

if dollars in range(1, 10):
    amount_in_words.append(numberdict[dollars])

print(f'{" ".join(amount_in_words)} and {cents}/100')