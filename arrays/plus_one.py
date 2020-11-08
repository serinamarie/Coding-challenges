# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # turn the digits into strings
        str_digit = [str(d) for d in digits]
        
        # question said tests wouldn't have a leading 0 but the last one does
        if all(elem=='0' for elem in str_digit):
            return [0]*(len(str_digit)-1) + [1]
        
        # join the strs and cast to int 
        joined_str = ''.join(str_digit)
        
        # before incrementing by 1 
        int_plus_one = int(joined_str) + 1
        
        # then casting to a str again
        new_int_as_str = str(int_plus_one)
        
        # return a list of ints
        return(int(char) for char in new_int_as_str)