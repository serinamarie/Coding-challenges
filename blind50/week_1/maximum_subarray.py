# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        max_subarray = nums[0]
        subarray = nums[0]
        for i in nums[1:]:
            if subarray < 0:
                subarray = 0
            subarray += i
            if subarray > max_subarray:
                max_subarray = subarray

        return max_subarray
    