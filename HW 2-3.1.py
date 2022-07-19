# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""Using nested control statements to analyze examination results"""

# initialize variables
passes = 0 # number of passes
failures = 0 # number of failures

# process 10 students
for student in range(10):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail): '))
    
    if result == 1:
            passes = passes + 1
    if result == 2:
            failures = failures + 1
    while result != 1 and result != 2:
        print('grade has not been entered correctly')
        result = int(input('Enter result (1=pass, 2=fail): '))
            
# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')
