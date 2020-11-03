# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # output should be a list of strings
        # input is a list of strings
        # constraints: must be in place
        
        # create end pointer
        right_pointer = len(s)-1
        
        # only iterate through first half (otherwise we'll just undo all our swaps)
        for left_pointer in range(len(s)//2): 
   
            # swaps their places
            s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
            
            # decrement right pointer
            right_pointer -= 1
            