# Given an integer array nums, return true if any value appears at least 
# twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # output: true, false
        # edge cases: nums length of 1
        # constraints: 
        # notes: it doesn't matter what the values are
        
        # we can't have a duplicate in an array of less than 2
        if len(nums) < 2:
            return False 
        
        length_nums = len(nums)
        length_unique_nums = len(set(nums))
        
        # if not same length, then we have a duplicate
        if length_nums != length_unique_nums:
            return True
    
        return False