# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # outputs: int
        # input: array
        # edge cases: array of length 1
        
        result = 0
        
        for i in nums:
            result ^= i
            
        return result