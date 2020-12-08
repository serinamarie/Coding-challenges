# Given a binary matrix A, we want to flip the image horizontally, then invert it, 
# and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. 
# For example, inverting [0, 1, 1] results in [1, 0, 0].

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        # output: list of lists of ints
        # input: list of list of ints
        # constraints: square matrix, values of 0 or 1
        # edge cases: if only 1x1 matrix
        
        # for row in matrix:
            # reverse row
            # invert the row
            # append the row to result
        
        # return result
        
        result = []
        
        # for each row in matrix
        for row in A:

            # reverse the row
            flipped = row[::-1]
            
            # create an empty array
            inverted_row = []
            
            # for each value in row
            for value in flipped:

                # invert the values
                if value == 0:
                    inverted_row.append(1)
                else:
                    inverted_row.append(0)

            # be sure to append the inverted row to the results before moving on to next row
            result.append(inverted_row)
        
        return result