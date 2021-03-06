# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # output: missing number
        # input: array 
        
        # sort nums
        # expected num
        
        # iterate through nums
            # compare expected num to actual num
            # if not equal, return expected
        
        expected = 0
        
        for num in sorted(nums):
            if num != expected:
                return expected
            else:
                expected += 1
        return expected
