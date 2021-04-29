'''
A peak element is an element that is greater than its neighbors. 
Given an input array nums, where nums[i] != nums[i + 1]
find a peak element and return its index.
The array may contain multiple peaks, in that case,
return the index to any one  of the peaks.
You may imagine tha nums[-1] = -inf

Example 1: 
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element nums[2] > nums[2 - 1] and nums[2] > nums[2 + 1]

Example 2: 
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: your function can return either index.

Note: Your solution should be in logarithmic (O(log n)) time complexity
'''

def getPeak(nums):
    l = 0
    r = len(nums) - 1

    while l < r:        
        mid = l + (r-l) // 2
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return l

print(getPeak([10,9,11,13,7,1]))