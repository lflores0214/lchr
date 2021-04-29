# Understand
# inputs: we are given a string in the form "k[encoded_string]"
# k is guaranteed to be a postive integer
# we want to take the encoded string inside the brackets and repeat it k number of times
# we can assume the input string is always valid 
# we can assume the input string does not contain any digits and digits are only used to indicate how many times the string should be repeated
# output: a decoded string 

# Plan 
# Since there will only be four types of characters, "letter", int, "[", "]"
# we can iterate through the given string and do different tasks depending on the character
# we can use the types of characters like opcodes 
# we will need to store the values in a stack 
# we need to build up the string to return 
# we can use the int to determine how many times to repeat the following string
# we will need to store the ints and letters as variables 
# string = "", num = 0, stack = []
# iterate through the string
# for char in input:
    # if the character is an int
        # store the int in num
        # we need to take into account an integer that is double digits 
        # eg. if the int is 2  num = 0 * 10 + 2 => num = 2
        # eg2. if the int is 25 num = 2 * 10 + 2 =? num = 25
        # num = num * 10 + int(char)
    # elif the character is a "["
        # append the current string to the stack 
        # stack.append(string)
        # append the current num to the stack 
        # stack.append(num)
        # we need to reset the string and num 
        # string = ""
        # num = 0
    # elif the char is a "]"
        # grab the num from the top of the stack
        # num = stack.pop
        # grab the previous string from the top of the stack
        # prev_string = stack.pop
        # update the current string 
        # string = prev_string + num * string 
    # else: the character is a letter
        # add the letters to the string
        # string = string. + char
    # return the string
    # return string

class Solution:
    def decodeString(self, s: str) -> str:
        string = ""
        # prev_string = ""
        num = 0
        stack = []
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            
            elif char == "[":
                stack.append(string)
                stack.append(num)
                
                string = ""
                num = 0
                
            elif char =="]":
                num = stack.pop()
                prev_string = stack.pop()
                string = prev_string + num * string
                
                num = 0
            
            else: 
                string = string + char
        
        return string
                
        
        
        
        
        
        
        
        