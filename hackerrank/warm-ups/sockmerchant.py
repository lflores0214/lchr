# understand
# inputs: are are give a number,n, and an array, arr
# n is an integer letting us know that amount of socks in the array
# the array contains n number of integers where each integer represents a color
# ie. 10 = red, 20 = blue, 30 = yellow, etc.abs
# we want to return the total number of pairs of matching socks in the array
# eg. if we are given an array [10 20 20 10 10 30 50 10 20] n = 9 because there are 9 socks in the pile
# we would be able to make total of 3 matching pairs (20, 20), (10,10), (10,10)

# plan
# we can itereate through the array and add each value to a dictionary
# each integer will be a key and the value will be the number of times that integer appears in the array
# we can then see how many times the integer appears and floor divide the value by 2 to get the number of pairs we can make
#then we add them up to see the total number of pairs we can make from the pile of socks 


def sockMerchant(n, ar):
    
    socks = {}
    
    for i in range(0,len(ar)):
        if ar[i] in socks:
            socks[ar[i]] += 1
        else:
            socks[ar[i]] = 1
    total = 0
    for sock in socks:
        if socks[sock] >= 2:
            total += socks[sock] // 2
    print(6//2)
    print(total)
    return total
my_arr = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]
sockMerchant(20, my_arr)

# reflecion:
# current runtime complexity is O(n) and space complexity is also O(n)
# I would like to see if there is a way to do this in one pass through the original array instead of putting values in a dictionary 
# runtime complexity would still be O(n) but space complexity would be O(1)