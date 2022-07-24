# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:24:34 2022

@author: jense
"""

one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
ten = 10
jack = 10
queen = 10
king = 10
ace = 11


name = [one, two, three, four, five, six, seven, eight, nine, ten, jack, \
        queen, king, ace]

(one, two, three, four, five, six, seven, eight, nine, ten, jack, queen, \
 king, ace) = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)

draw1 = random.choice(name)
draw2 = random.choice(name)

print(draw1, name)
print(draw2, name)
print('total:', draw1 + draw2)

if draw1 + draw2 <= 21:
        print('good job!')
if draw1 + draw2 > 21:
        print ('better luck next time!')
        

        

        

