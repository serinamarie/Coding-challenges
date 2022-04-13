# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral 
# for four is not IIII. Instead, the number four is written as IV. Because the one is before the 
# five we subtract it making four. The same principle applies to the number nine, which is written 
# as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        # examples I, IV, CM (900), XLIV (44)
        # input: string, output: integer
        # constraints: it won't be empty string, can be up to 15 chars
        
        numeric_array = []
        
        # store 7 letters in hash map
        romans = {
            'I':1, 
            'V':5, 
            'X':10, 
            'L':50, 
            'C':100, 
            'D':500, 
            'M':1000
        }
        

        # iterate through reversed string
        for char in s[::-1]:
            numeric_value = romans[char]
            if not numeric_array:
                numeric_array.append(numeric_value)
            # if the last value of the array is larger than the current char's numeric value
            elif numeric_array[-1] > numeric_value:
                # append the negated numeric_value
                numeric_array.append(-numeric_value)
            else:
                numeric_array.append(numeric_value)
                
        return sum(numeric_array)