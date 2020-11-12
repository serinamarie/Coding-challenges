# Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # input: list of ints, k as int
  
        # first pass solution
        # while k > 0:
        #     to_first_index = nums.pop()
        #     nums.insert(0, to_first_index)
        #     k -= 1
          
        # in-place solution
        # ii = 0 
        # # iterate through reversed list 
        # # moving everything to the left k times
        # for _ in nums[::-1]:
        #     next_num = nums[ii+1]
        #     nums[ii+1] = nums[ii]
        #     ii += 1
            
        # e.g. 
        # nums = [1,2,3,4,5,6,7], k = 3
        

        k = k % len(nums)
        if not k:
            return
        
        # rotating to the right
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
        # start from k before end, and make it the the first k values
        # start from the beginning until we are k before end and make it the values starting at index k 