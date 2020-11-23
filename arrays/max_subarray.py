# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# Follow up: If you have figured out the O(n) solution, try coding another 
# solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # output: largest sum of subarray
        # input: list of ints
        # constraints: length of 1 
        # keep track of the sum as you go
        
        # set maxes to first num in array (not 0, as we may have an array made of solely negative ints)
        greatest_max = nums[0]
        current_max = nums[0]
        
        for i in range(len(nums)):
            
            # which is greater: the current num or the running total so far + the current num 
            current_max = max(current_max + nums[i], nums[i])
            
            # is the current_max greater than our greatest_max we've found so far?
            greatest_max = max(greatest_max, current_max)
            
        # return greatest_max
        return current_max
  
        
        # other ideas:
        # keep trying to expand the array while keeping track of the largest contiguous sum
        

        
        