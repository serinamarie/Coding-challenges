# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # output: boolean
        # input: array
        # edge cases: empty array
        
        cache = {}
        
        for num in nums:
            if num not in cache:
                cache[num] = 1
            else:
                return True
    
        return False
    
        # alternatively,
        # if len(set(nums)) != len(nums):
        #     return True