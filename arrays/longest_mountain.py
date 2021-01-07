class Solution:
# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. 
# Return 0 if there is no mountain subarray.


    def longestMountain(self, arr: List[int]) -> int:
        # output: int of mountain size
        # input: array
        # constraints: no empty arrays, values are >= 0
        # edge cases: array of length 1 must work
        
        # keep track of longest mountain as we iterate through
        
        # if we have no mountains we'll return 0
        longest_mountain = 0
        
        # iterate through
        for i in range(1, len(arr)-1):
            
            # if the values on both sides of i are less than i
            if arr[i-1] < arr[i] > arr[i+1]:

                # set two pointers, l and r, equal to i
                l = r = i
                
                # while the values to the left of i continue to be less and less
                while l > 0 and arr[l] > arr[l-1]:

                    # decrease our l index pointer
                    l -= 1
         
                # while the values to the right of i continue to be less and less
                while r + 1 < len(arr) and arr[r] > arr[r+1]:
                    
                    # increase our r index pointer
                    r += 1
                   
                # if our current subarray is longer than the longest mountain we've found so far, 
                # make that the new longest_mountain
                longest_mountain = max(longest_mountain, (r-l +1))
        
        return longest_mountain
                    
                    