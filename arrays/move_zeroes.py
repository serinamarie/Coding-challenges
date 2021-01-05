# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note:

    # You must do this in-place without making a copy of the array.
    # Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # output: return nothing
        # input: array
        # constraints: in-place
        # edge cases: empty array, one without 0s in it, maybe one with all 0s
        # counter = 0
      
        j = 0

        # for item in range
        for i in range(len(nums)):

            # if the value is not 0
            if nums[i] != 0:
                # make the value into the index at j
                nums[j]= nums[i]
                # increment the j
                j += 1
        
        # for item in range of j to the end of the array
        for index in range(j, len(nums)):
            
            # make that index 0
            nums[index] = 0

        