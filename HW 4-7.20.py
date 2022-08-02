# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 23:53:26 2022

@author: jense
"""

import random

%timeit rolls_list = [random.randrange(1, 7) for i in range (0, 6_000_000)]

import numpy as np

%timeit rolls_array = np.random.randint(1, 7, 6_000_000)

%timeit rolls_list = [random.randrange(1, 7) for i in range (0)]
%timeit rolls_list = [random.randrange(1, 7) for i in range (0, 10)]
%timeit rolls_list = [random.randrange(1, 7) for i in range (0, 100)]
%timeit rolls_list = [random.randrange(1, 7) for i in range (0, 1_000)]
%timeit rolls_list = [random.randrange(1, 7) for i in range (0, 10_000)]
%timeit rolls_list = [random.randrange(1, 7) for i in range (0, 100_000)]
%timeit rolls_list = [random.randrange(1, 7) for i in range (0, 1_000_000)]

%timeit rolls_array = np.random.randint(1, 7, 0)
%timeit rolls_array = np.random.randint(1, 7, 10)
%timeit rolls_array = np.random.randint(1, 7, 100)
%timeit rolls_array = np.random.randint(1, 7, 1_000)
%timeit rolls_array = np.random.randint(1, 7, 10_000)
%timeit rolls_array = np.random.randint(1, 7, 100_000)
%timeit rolls_array = np.random.randint(1, 7, 1_000_000)
