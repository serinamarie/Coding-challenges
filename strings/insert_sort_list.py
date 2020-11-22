# Sort a linked list using insertion sort.

# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition, 
# # and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, 
# finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.


# First pass solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # output: sorted LL
        # input: unsorted LL
        # edge cases: single node, empty LL, (could there be nodes of equal value??)
        
        # e.g. 
        # Input: 4->2->1->3
        # Output: 1->2->3->4
        
        # dump all values into an array
        arr = []
        
        if not head:
            return 
        
        while head:
            arr.append(head.val)
            head = head.next
        
        # loop through array to sort
        for i in range(1, len(arr)):
            
            # store the current value
            current = arr[i]
            
            # copy that index
            j = i
            
            # as long we are within range AND while our current value is smaller than the value before it (meaning it's out of order)
            while j > 0 and current < arr[j-1]:
                # swap the values
                arr[j] = arr[j-1]
                
                # decrement j to find the proper index (since the value is too small to be at its current slot)
                j -= 1
                
            # once we've found the proper index, store the value there
            arr[j] = current
                
                                
        # create new LL with sorted values
        curr = sorted_ll = ListNode(arr[0])
        
        for i in arr[1:]:
            curr.next = ListNode(i)
     
            curr = curr.next
     
        return sorted_ll        