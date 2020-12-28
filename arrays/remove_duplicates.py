# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # input: array
        # output: length of shortened array, and the array itself
        # constraints: length between 0 and 3*10^4, values between -10^4 and 10^4
        # nums are sorted
     
        # edge cases: length of 0, length of 1, no extra memory
        
        # if the array is empty return
        # if array is of length 1: return
        
        jj = 0
        
        for ii in range(1, len(nums)):
            # compare the previous value with the current value
            # if they are not equal
            if nums[jj] != nums[ii]:
                # increment the j
                jj += 1
                nums[jj] = nums[ii]

        # return new length     
        return jj + 1

        # e.g.
        # jj = 5
        # ii  = 7
        # [0,1,2,2,3,3,4]
        # [0,1,2,3,4]