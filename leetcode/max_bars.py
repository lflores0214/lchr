"""
It is a sweltering summer day, and a boy wants to buy some ice cream bars.

At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Return the maximum number of ice cream bars the boy can buy with coins coins.

Note: The boy can buy the ice cream bars in any order.
"""


def max_ice_cream(costs: "list[int]", coins: int) -> int:
    if coins < min(costs):
        return 0

    if coins >= sum(costs):
        return len(costs)

    bars: int = 0
    price: int =0
    for i in range(len(costs)):
        price += costs[i]
        if price <= coins:
            bars += 1
        else:
            break

    return bars
