def isValid(s):
        if s == "":
            return True
        
        
        stack = []
        chars_to_push = ["(", "{", "["]
        
        for i in range(0, len(s)):
            if s[i] in chars_to_push:
                stack.append(s[i])
            elif s[i] == "]" and len(stack) != 0:
                if stack.pop() != "[":
                    return False
            elif s[i] == ")" and len(stack) != 0:
                if stack.pop() != "(":
                    return False
            elif s[i] == "}" and len(stack) != 0:
                if stack.pop() != "{":
                    return Fasle
        if len(stack) > 0:
            return False
        else:
            return True

arr =["(", ")"]

print(isValid(arr))