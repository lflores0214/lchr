# import math
# def countTriplets(arr, r):
#     count = 0
#     possibilities = {}
#     combos = {}
    
#     for number in arr:
#         num2 = number * r
#         num3 = num2 * r
#         possibilities[number] = (number, num2, num3)
#     for i in range(0, len(arr)):
        
#         if combos.get(arr[i]):
#             temp = combos[arr[i]]
#             temp2 = (i,)
#             combos[arr[i]] = temp + temp2
#         else:
#             combos[arr[i]] = (i,)
#     # if len(combos) == 1:
#     #     return len(arr)
#     for key,value in possibilities.items():
#         # print("pos", possibilities)
#         # print("val",value)
#         # print("val1",value[1])
#         # print("this",combos.get(value[0][0]))
#         # print("this1",combos.get(value[0][1]))
#         # print("this2",combos.get(value[2]))
#         if combos.get(value[0]) and combos.get(value[1]) and combos.get(value[2]):
            
#             num = 1
#             if len(combos[value[0]]) >1:
#                 num = max(num, len(combos[value[0]]))
            
#             if len(combos[value[1]]) >1:
#                 num = max(num, len(combos[value[1]]))
            
#             if len(combos[value[2]]) >1:
#                 num = max(num, len(combos[value[2]]))
#             count += num
#     # print(combos)
#     # print(possibilities)

    
#     return count

# my_arr = [1] * 100
# r = 1
# print(countTriplets(my_arr, r))
# print(161700 * 100)

# from collections import Counter
# def countTriplets(arr, r):
#     r2 = Counter()
#     r3 = Counter()
#     count = 0
#     print("r2", r2)
#     print("r3", r3)
#     for v in arr:
#         if v in r3:
#             count += r3[v]
#         if v in r2:
#             r3[v*r] += r2[v]
#         r2[v*r] += 1
    
#     return count
from collections import defaultdict
# def countTriplets(arr, r):
#     v2 = defaultdict(int)
#     v3 = defaultdict(int)
#     print("v2", v2)
#     print("v3", v3)
#     count = 0
#     for k in arr:
#         count += v3[k]
#         v3[k*r] += v2[k]
#         v2[k*r] += 1
#     print("v2", v2)
#     print("v3", v3)
#     return count
# arr = [1,2,2,4]
# r = 2
# print(countTriplets(arr, r))
def countTriplets(arr, r):
    # stores number of tuples with two elements that can be formed if we find the key
    potential_two_tuples = defaultdict(int) 
    # stores number of tuples with three elements that can be formed if we find the key
    potential_three_tuples = defaultdict(int)
    count = 0
    for k in arr:
        # k completes the three tuples given we have already found k/(r^2) and k/r  
        count += potential_three_tuples[k]
        # For any element of array we can form three element tuples if we find k*r given k / r is already found. Also k forms the second element.
        potential_three_tuples[k*r] += potential_two_tuples[k]
        # For any element of array we can form two element tuples if we find k*r. Also k forms the first element.
        potential_two_tuples[k*r] += 1 
    return count
arr = [1,5,5,25,125]
r = 5
print(countTriplets(arr, r))