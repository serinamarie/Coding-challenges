# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:

# It is guaranteed that there are no cycles anywhere in the entire linked structure.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # output: node where intersects
        # input: two node heads
        # constraints: if not intersects,return 0
        # the head will not be where intersects
        
        # iterate through LL B, store node values in a separate set O(len(A))
        # iterate through LL A, if node in set, return node
        b_nodes = set()
        
        while headB is not None:
            b_nodes.add(headB)
            headB = headB.next
        while headA is not None:
            if headA in b_nodes:
                return headA
            headA = headA.next