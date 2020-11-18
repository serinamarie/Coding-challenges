# Given a string s, the power of the string is the maximum length 
# of a non-empty substring that contains only one unique character.

# Return the power of the string.

class Solution:
    def maxPower(self, s: str) -> int:
        # output: len of max substring of consecutive char as int
        # input: str
        # constraints: length from 1-500, only lowercase english letters
        # edge cases: must work for length of 1
        
        # keep track of the max length as we go, and also have a current max length
        # greatest max = 1
        # loop through string (while next char)
        # if next char is equal to current char:
            # increase local max
            # if local max is greater than the greatest max
                # greatest max = greatest max
        # return greatest max
        
        # the lowest possible max would be 1
        greatest_max = 1
        local_max = 1
        
        for i in range(len(s)-1):

            # if the next char is same as current char
            if s[i+1] == s[i]:

                # increase local max
                local_max += 1

                # if local max has exceeded greatest max found so far 
                if local_max > greatest_max:

                    # update the greatest max
                    greatest_max = local_max

            # if next char is different from current char
            else:

                # reset local max and move on to next i
                local_max = 1
                
        return greatest_max
                