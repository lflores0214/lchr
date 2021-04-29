# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Understand
# Inputs: two sorted linked lists -> 1->2->4, 1->3->4
# merge the two linked lists in sorted order
# output: the two sorted linked lists merged into one sorted linked list -> 1->1->2->3->4->4

# Plan 
# create a head node for the new merged list 
# create a pointer for the new merged_list
# create pointers for the two linked lists we recieve as inputs
# check if the value of the first input (l1) is smaller the the value of the second input, (l2)
# while l1 and l2 have values
# if the value of the l1 node is smaller than  or equal to the value of the l2 node 
    # then we make l1 the node for merged_list.next
    # move the l1 pointer to point to the next node in the list 
    # move the merged list pointer to next
# else if the value of the l1 node is larger 
    # then we make l2 the node for merged_list.next
    # move the l2 pointer to pointer to the next node in the list
    # move the merged list pointer to next 
# we need a check in case one list is longer than the other 
    # if l1 has no value then we can assume that we just need to add the rest of l2 and vice versa
    # if l1 is None 
        # merged_list.next is l2
    # else if l2 is none 
        # merged_list.next is l1



class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged_list = ListNode(0)
        head = merged_list
        
        # pointer1 = l1
        # ponter2 = l2
        
        while l1 is not None and l2 is not None:
            smaller_value = 0
            if l1.val <= l2.val:
                smaller_value = l1.val
                l1 = l1.next
            else:
                smaller_value = l2.val
                l2 = l2.next
            head.next = ListNode(smaller_value)
            head = head.next
        if l1 is None:
            head.next = l2
            # l2 = l2.next
        elif l2 is None:
            head.next = l1
            # l1 = l1.next
            
        return merged_list.next