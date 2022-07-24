# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:52:10 2022

@author: jense
"""

a = [[83, '\t', 'Electric sander', 7, '\t', '57.98'], [24, '\t', \
     ...:'Power saw', '\t', 18, '\t', '99.99'], [7, '\t', '\t', 'Sledge hammer', \
     ...:11, '\t', '21.50', '\t'], [77, '\t', 'Hammer', '\t', '\t', 76, '\t', \
     ...:'11.99'], [39, '\t', 'Jig saw', '\t', '\t', 3, '\t', '79.50']]
    
print('Part no.', 'Part description', 'Quantity', 'Price')
for row in a:
    for item in row:
        print(item, end='  ')
    print()

# a

from operator import itemgetter

itemgetter('Part description')

# b

from operator import itemgetter

itemgetter('Price')

# c




