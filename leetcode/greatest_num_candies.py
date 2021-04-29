"""
Input: list of number of candies each kid has. Kid number cooresponds with array position.
        extraCandies = n, extra candies each kid can receive.
Output: a list of booleans where True will be if that kid has the highest number of candies
        - multiple kids can have the highest number of candies.
        - eg. [3,4,1,2,4] -> kids at position 1, and 4 have the highest number of candies 
"""


def kids_with_candies(candies: "list[int]", extraCandies: int) -> "list[bool]":
    res: "list[bool]" = [bool for _ in candies]

    for x in range(len(candies)):
        if candies[x] + extraCandies >= max(candies):
            res[x] = True
        else:
            res[x] = False
    return res


candies = [4,2,1,1,2]

print(kids_with_candies(candies, extraCandies=1))
