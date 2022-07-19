# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 20:05:50 2022

@author: jense
"""

# these are my notes

print('amount on deposit at the end of 10 years:', 1000 * (1 + 0.07) ** 10)
print('amount on deposit at the end of 20 years:', 1000 * (1 + 0.07) ** 20)
print('amount on deposit at the end of 30 years:', 1000 * (1 + 0.07) ** 30)

total = (1000 * (1 + 0.07))
for number in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30):
    total = total ** number    
print('')

# this is my final answer

p = 1000
r = 0.07

for year in range(31):
    print(f'Amount after {year} year(s): {p * (1 + r) ** year:.2f}')
    