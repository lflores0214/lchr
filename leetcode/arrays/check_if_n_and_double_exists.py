"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.

 

Constraints:

    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3


"""



def checkIfExist(arr):
    hashtable = {}
    n = len(arr)-1
    for i in range(n):
        if arr[i] not in hashtable:
            hashtable[arr[i]] = i
        
        if arr[i] * 2 in hashtable and hashtable[arr[i] * 2] != i:
            return True        
        if arr[i] / 2 in hashtable and hashtable[arr[i] / 2] != i:
            return True
    return False

arr1 = [10,2,5,3]
arr2= [-2,0,10,-19,4,6,-8]
arr3 = [-20,8,-6,-14,0,-19,14,4]
arr4 = [0,0]
# print(checkIfExist(arr1))
# print(checkIfExist(arr2))
print(checkIfExist(arr3))