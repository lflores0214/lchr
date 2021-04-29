#!/bin/python3

import math
import os
import random
import re
import sys



# understand:
# inputs: we are given an array with two values, D and U 
# when we hit a D in the array it means the hiker is heading down 
# when we hit a U in the array it means the hiker is heading up
# the hiker starts at sea level and we want to know how many valleys the hiker has traversed 
# each value in the array represents 1 unit change in altitude 
# for example if the value of an array is U the hiker went up 1 unit of altitude 
# if the calue was D the hiker went down 1 unit of altitude
# outputs: a sibgle integer indicating how many valleys the hiker traveresed 

# plan:
# we can set two variables, valleys and altitude, to 0
# itereate through the array 
# for i in range(n)
#   check if we have a U or D 
#   if s[i] == U:
    #   check if the altitude is at -1
    #   if altitude == -1:
            # we increment the number of valleys since the hiker got back up to sea level
            # valleys += 1
#   if we have a D then just decrement the altitude
#   else:
#       altitude -= 1
# return the number of valleys
# return vallys


# Complete the countingValleys function below.
def countingValleys(n, s):
    
    altitude = 0 
    
    valleys = 0

    for i in range(0, n):
        if s[i] == "U":
            if altitude == -1:
                valleys += 1
            altitude += 1
        else:
            altitude -= 1
    return valleys
       

               
                

