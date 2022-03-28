# Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        # keep track of what the current index is
        # keep track of values not at current index  
        cached = {}
        
        for i in range(len(nums)):
            current_value = nums.pop(i) 
            if current_value in cached:
                answer.extend([cached[current_value]])
            else:  
                product = 1
                for num in nums:
                    product *= num
                answer.extend([product])
                cached[current_value] = product
            nums.insert(i, current_value)
                
        return answer