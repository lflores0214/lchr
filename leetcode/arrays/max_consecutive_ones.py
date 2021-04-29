'''
Given a binary array, find the maximum number of consecutive 1s in this array.
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000


'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        highest = 0
        current = 0
        for i in range(n):
            if nums[i] == 1:
                current+= 1
            else:
                if current >= highest:
                    highest = current
                current = 0
        if current > highest:
            return current
        return highest