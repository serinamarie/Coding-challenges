# Given head which is a reference node to a singly-linked list. 
# The value of each node in the linked list is either 0 or 1. 
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # output: decimal int
        # input: reference node to LL
        # constraints: nodes' values 0 or 1. no more than 30 nodes. no empty LL
        # edge cases: if no next (single node)
        
        # e.g. head = [1,0,1]
        # output: 5
        
        str_dec = ''
        
        # loop through each node, adding value to linked list
        while head:
            str_dec += str(head.val)
            head = head.next
            
        # convert the str_dec to int, convert to dec int(result, 2)
        # return result
        return int(str_dec, 2)
