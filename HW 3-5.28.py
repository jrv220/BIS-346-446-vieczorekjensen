# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 22:18:06 2022

@author: jense
"""


r = (1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5)

dict((i, r.count(i)) for i in r) 

import numpy as np
import statistics as stats

values, counts = np.unique(r, return_counts=True)
values = list(values)
counts = list(counts)

print('Reponses and frequencies:')
for value, count in zip(values, counts):
    print(f'{value}: {count}')

print(f'Min response count: {values[counts.index(min(counts))]} occurred \
      {min(counts)} time(s)')
print(f'Max response count: {values[counts.index(max(counts))]} occurred \
      {max(counts)} time(s)')
print(f'Range of response counts: {min(counts)}-{max(counts)}')
print(f'Mean response count: {stats.mean(counts)}')
print(f'Median response count: {stats.mean(counts)}')
print(f'Mode response count: {stats.mode(counts)}')
print(f'Variance: {stats.pvariance(counts)}')
print(f'Standard deviation: {stats.pstdev(counts)}')