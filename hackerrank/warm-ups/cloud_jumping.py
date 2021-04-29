
import math
import os
import random
import re
import sys


#understand:
# inputs:
# we are given an array of binary numbers 0's and 1's
# we have to traverse through the array while avoiding the 1's 
# we can jump one or two indices at a time 
# we want to return the minimum number of jumps required to make it to the end
# output: 
# an integer indicating the minimum number of jumps required

# plan:
# given an array c = [array of binary numbers]
# we can keep a counter for our current position
# position = 0
# we can keep a jump counter to keep track of our jumps
# jumps = 0
# we can check if the index two numbers away is a 1 
# if c[position + 2] == 1:
#   if it is then just jump 1 spot 
#   position += 1
#   increment the jumps
#   jumps += 1
# else if the the index two numbers away is a zero then we can jump there
# else:
#   posistion +=2
#   increment the jumps
#   jumps += 1
# return the jumps
# return jumps
    


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    position = 0
    jumps = 0
    
    while position < len(c) -1:
        if position == len(c)-2:
            position += 1
            jumps += 1
        elif c[position + 2] == 1 or c[position + 2] == None:
            position += 1
            jumps += 1
        else:
            position += 2
            jumps += 1
    return jumps

my_arr = [0, 0, 0, 1, 0, 0]
jumpingOnClouds(my_arr)