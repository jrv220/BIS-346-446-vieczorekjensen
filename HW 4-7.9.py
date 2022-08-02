

import numpy as np

numbers = np.arange(1, 16).reshape(3, 5)

type(numbers)

numbers

# a. select row 2

numbers[2]

# b. select column 4

numbers[:, 4]

# c. select rows 0 and 1

numbers[:, 0:2]

# d. select columns 2-4

numbers[:, 2:5]

# e. select the element that is in row 1 and column 4

numbers[1, 4]

# f. select all elements from rows 1 and 2 that are in columns 0, 2 and 4

numbers[1:3, [0, 2, 4]]
