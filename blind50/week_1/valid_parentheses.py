# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
        expected_close = ''
        openers = "([{"
        
        oc_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
       
        # iterate through
        for char in s:
            if char in openers:
                expected_close = oc_dict[char] + expected_close
            else:
                if expected_close:
                    if expected_close[0] == char:
                        if len(expected_close) > 1:
                            expected_close = expected_close[1:]
                        else:
                            expected_close = ''
                    else:
                        return False
                else:
                    return False
                    
        # expected_close should be empty
        if not expected_close: 
            return True
        else:
            return False