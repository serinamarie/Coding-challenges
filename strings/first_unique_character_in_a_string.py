# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
# Note: You may assume the string contains only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # output: index as type int
        # input: s as type string
        # constraints: optimize run time, so ideally, O(n)
        # edge cases: no unique chars (return -1), empty string, very long string
        
        # iterate through string to find first unique char's index

        # get a set of all unique chars     
        chars = set(s)

        # if the count is equal of a char is 1, get the index
        index = [s.index(char) for char in chars if s.count(char) == 1] or [-1]

        # return the first index
        return min(index) 
        

            