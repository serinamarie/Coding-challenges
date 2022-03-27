# Given an array of integers nums and an integer target, return indices of the two 
# numbers such that they add up to target. You may assume that each input would 
# have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # edge cases: target is negative int, length of nums is 2
        # plan:
        # get index of first two nums
        # total - current_index value 
        for i in range(0,len(nums)):
            addend = target - nums[i]
            for y in range (i+1, len(nums)):
                if nums[y] == addend:
                    return [i,y]
                