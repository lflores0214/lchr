'''
Suppose an array sorted in ascending order is rotated ar some pivot unknown to you beforehand.
ie. [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]
Find the minimum element 
You may assume no duplicate exists in the array

Example 1:
Input: [3,4,5,1,2]
output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
output: 0
'''


def getMin(nums):
    if len(nums) == 0:
        return -1

    if len(nums) == 1:
        return nums[0]

    l = 0
    r = len(nums) - 1

    while l < r:
        mid = l + (r - l) //2

        if mid > 0 and nums[mid] < nums[mid - 1]:
            return nums[mid]
        elif nums[l] <= nums[mid] and nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid =1

    return nums[l]


print(getMin([3,4,5,1,2]))
