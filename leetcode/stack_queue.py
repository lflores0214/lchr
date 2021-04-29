# understand: 
# implement the functions of a queue using stacks
# push(x) => pushes x to the back of the que
# pop() => removes the element from the front of the queue
# peek() => get the front element
# empty() => checks if the queue is empty

#Plan: 
# initialize the MyQueue class with two stacks, one for pushing and for popping
# push: 
    #append the input to the push stack
# pop:
    # check if the pop stack is empty
    # if it is
        # while the the push stack is not empty 
        # pop from the push stack and append what you just popped to the pop stack
    # pop the last element from the pop and return what you just popped 
# peek: 
    # check if the pop stack is empty
    # if it is
        # while the the push stack is not empty 
        # pop from the push stack and append what you just popped to the pop stack
    # return the last element from the pop stack
# empty:
    # check if either of the stacks are empty
        # if one of them has something in them the queue is not empty
            # return False
        # else
            # return True if both stacks are empty
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.push_stack.append(x)
        
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.pop_stack) == 0:
            while len(self.push_stack) > 0:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack.pop()
    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.pop_stack) == 0:
            while len(self.push_stack) > 0:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]
            
            
            

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.push_stack) > 0 or len(self.pop_stack) > 0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()