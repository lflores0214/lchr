'''
Given an Array A of distinct integers sorted in ascending order, 
return the smallest index i that satisfies A[i] == i. 
return -1 if no such i i exists

Example 1:
Input : [-10, -5, 0, 3, 7]
Output: 3
Explanation: For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3

Example 2: 
Input: [0,2,5,8,17]
Output: 0
Explanation: For the given array A[0] = 0

Example 3: 
Input: [-10, -5, 3, 4, 7, 9]
Output: -1
Explanation: There is not such i where A[i] = i, thus the output is -1

'''


def fixedPoint(arr):
    l = 0
    r = len(arr) - 1
    while l + 1 < r:
        mid = l+(r+l) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            l = mid
        else:
            r = mid
    


arr1 = [-10, -5, 0, 3, 7]
arr2 = [0,2,5,8,17]
arr3 = [-10, -5, 3, 4, 7, 9]