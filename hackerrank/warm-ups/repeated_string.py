#!/bin/python3

import math
import os
import random
import re
import sys

# understand 
# inputs: we are given a string, s, of lowercase letters, and an integer, n
# the string gets repeated until the string is length of n
# eg. given s = "aabc", and  n = 10, the new string will be "aabcaabcaa"
# we want to find the number of a's in the new string
# output: an integer indicating the number of a's in the new string

# plan
# create a new string 
# new_string = ""
# create a counter for the a's
# a_count = 0
# see how many times the len(string) can go into n 
# num = n // len(s)
# remainder = n % len(s)
# get the remainder and splice the first string up to the remainder into the new string
# then iterate through the new string and increment the a_count whenever we hit an a
# return  a_count

# original plan didn't pan out.
# memory limits were being reached because of insanely long strings
# we will have to figure it out without actually building the string
# so we still have to get the number of times the string can go into n and the remainder
# num = n // len(s)
# remainder = n % len(s)
# we itereate through the original string and count how many a's are there
# then we multiply by num to see how many a's there will be if we actually built out the string
# then we just iterate through the remaining string ie. s[:remainder] and count the a's in there 
# return the final count



# Complete the repeatedString function below.
def repeatedString(s, n):
    a_count = 0
    total = 0

    if s == "a":
        return n
    else:
        for i in s:
            if i == "a":
                a_count += 1
    
    num = n // len(s)
    remainder = n % len(s)

    total += a_count * num
    sub_string = s[:remainder]
    
    for i in sub_string:
        if i == "a":
            total += 1
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
