# Given two strings s and t , write a function to determine if t is an anagram of s.

# Note: You may assume the string contains only lowercase alphabets.

# Follow up: What if the inputs contain unicode characters? How would you adapt your solution to such case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # output: bool
        # input: two str
        # constraints: lowercase alphabet
        # edge cases: empty strs
        
        # both strings are empty
        if not s and not t:
            return True
        
        # if lengths are different
        elif len(s) != len(t):
            return False
  
        # otherwise iterate through string characters
        for char in s:

            # remove each char in s from t 
            t = t.replace(char, '', 1)

            # if we now have an empty t
            if not t:

                # they are anagrams!
                return True
                
        # if we have finished iterating and still have remaining letters in t, they are not anagrams
        return False