#!/bin/python3

import math
import os
import random
import re
import sys

# understand
# inputs: an array, a , and an integer, d
# We want to rotate the array, a, d number of times to the left
# eg. giiven an array a = [1,2,3,4,5] and an int d=4 we want to rotate a, 4 times to the left
# [1,2,3,4,5] -> [2,3,4,5,1] -> [3,4,5,1,2] -> [4,5,1,2,3] -> [5,1,2,3,4]
# [5,1,2,3,4] would be our desired outcome 
# output a single line of n, space seperated integers

# plan
# make a new array to store the rotated array
# rotated_array = []
# iterate through the array from the dth spot first 
# for i in range(d, len(a))
#   append the values to the rotated array as you go through them
#   rotated_array.append(a[i])
# the niterate through the original array up to the dth spot
# for in range(0, len(a[:d])):
#   append the values to the rotated array as you go through them
#   rotated_array.append(a[i])
# then just return the rotated_array
# return the rotated arr


# Complete the rotLeft function below.
def rotLeft(a, d):
    rotated_array = []

    
    for i in range(d, len(a)):
        rotated_array.append(a[i])

    for i in range(0, len(a[:d])):
        rotated_array.append(a[i])

    return rotated_array




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
