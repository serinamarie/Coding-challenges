# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate through o(n)
        # add key,v to dict
        
        cache = {} # o(n)+
        
        for s in strs: # o(n)
            ordered_s = ''.join(sorted(s))
            if ordered_s in cache:
                cache[ordered_s].append(s)
            else:
                cache[ordered_s] = [s]
                
        
        res = [] # o(n)
        for v in cache.values():
            res.append(v)
            
        return res