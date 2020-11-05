# Given two arrays, write a function to compute their intersection.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # outputs: single list of ints
        # inputs: two lists of ints
        # constraints: 
        # edge cases: one or both inputs are empty, return []
        
        # create an empty list
        intersection = []
        
        # for each number in our first array
        for x in nums1:
            # if it is also in our second array
            if x in nums2:
                # append it to our intersection list
                intersection.append(x)
                # then remove it from our second list, that way we 
                # can ensure duplicate ints are properly handled
                nums2.remove(x)
          
        # return matching numbers
        return intersection
    
       
        
           
        
  