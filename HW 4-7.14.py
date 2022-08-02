# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 23:51:13 2022

@author: jense
"""

import numpy as np

array1 = np.array([[0, 1], [2, 3]])
array2 = np.array([[4, 5], [6, 7]])


array3 = np.vstack((array1, array2))

array3

array4 = np.hstack((array1, array2))

array4

array5 = np.vstack((array4, array4))

array5

array6 = np.hstack((array3, array3))

array6
