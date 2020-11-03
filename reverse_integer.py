# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        # output: int
        # input: int
        # constraints: -2**31 to 2**31 - 1
        # edge cases: a single number, a zero, a negative number
        
        INT_MAX = 2**31-1
        
        # reverse result by casting to str type (also use absolute so we aren't dealing with a hyphen in the string)
        reversed_str = str(abs(x))[::-1]
        # return to int, now reversed
        reversed_int = int(reversed_str)
        
        # check if less than max (don't need to worry about min constraint since we used abs)
        if reversed_int > INT_MAX:
            return 0
        
        if x < 0:
            return -reversed_int
        
        # if a positive int and within constraints
        return reversed_int