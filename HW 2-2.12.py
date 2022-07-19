# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 20:05:17 2022

@author: jense
"""

# these are my notes for this problem

p = 1000
r = 0.07
n = 10, 20, 30


p(1 + r) ** 10

print('amount on deposit at the end of 10 years:', p(1 + r) ** 10)
print('amount on deposit at the end of 20 years:', p(1 + r) ** 20)
print('amount on deposit at the end of 30 years:', p(1 + r) ** 30)

print('amount on deposit at the end of 10 years:', 1000(1 + 0.07) ** 10)
print('amount on deposit at the end of 20 years:', 1000(1 + 0.07) ** 20)
print('amount on deposit at the end of 30 years:', 1000(1 + 0.07) ** 30)

# this is my final answer

print('amount on deposit at the end of 10 years:', 1000 * (1 + 0.07) ** 10)
print('amount on deposit at the end of 20 years:', 1000 * (1 + 0.07) ** 20)
print('amount on deposit at the end of 30 years:', 1000 * (1 + 0.07) ** 30)