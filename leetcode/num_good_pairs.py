"""
Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
"""


def num_identical_pairs(nums: "list[int]") -> int:
    count = 0

    for i in range(len(nums) - 1):
        for j in range(len(nums)):
            if j > i and nums[i] == nums[j]:
                count += 1

    return count

