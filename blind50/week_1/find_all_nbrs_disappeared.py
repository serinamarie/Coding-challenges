# Given an array nums of n integers where nums[i] is in the range [1, n], return 
# an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # thoughts: if you have an array of length 8, you know the max int <= 8
        # in array [1,1] we expect to see a 2. 
        # sorting the array may be best way to not use extra space
        # edge cases: empty array, array of length 1 
        
        # plan:
        # or instead of sorting, if know the length is the expected max, we could
        # create a dict of lenth nums
        # if the n in nums isn't in the dict
        # add to res array
        # return the res array

        # create a dict of lenth nums
#         nums_dict = {}
#         for k in set(nums):
#             nums_dict[k] = '_'

#         res = []
#         for n in range(1,len(nums)+1):
#             if n not in nums_dict:
#                 res.append(n)

#         return res
                
        for i in range(len(nums)):
            # if nums[0] = 4, we want to mark the 4th element in the array as 'seen'
            seen_idx = abs(nums[i]) - 1
            # if we haven't seen the number, negate the number
            if nums[seen_idx] > 0:
                nums[seen_idx] = -nums[seen_idx]
            # if we have already seen it, ignore it
  
        # any positive nbrs have not been seen and are therefore not in the array
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        
        return res