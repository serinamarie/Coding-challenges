# We have n chips, where the position of the ith chip is position[i].

# We need to move all the chips to the same position. In one step, we 
# can change the position of the ith chip from position[i] to:

# position[i] + 2 or position[i] - 2 with cost = 0.
# position[i] + 1 or position[i] - 1 with cost = 1.
# Return the minimum cost needed to move all the chips to the same position.
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # output: int
        # input: array
        # constraints: input not empty
        # edge cases: if len(input) is 1, return 0, equal number of odds/evens 
        
        # get parity counts
        # return minority
        
        # we start with no evens or odds
        evens = 0
        odds = 0
        
        # iterate through
        for num in position:

            # if num is even
            if num % 2 == 0:
                evens += 1

            # if num is odd
            else:
                odds += 1
        
        # return the minority, as we will end up moving these minority chip parity 
        # for a cost of 1 each to make them the same parity as the majority
        return min(evens, odds)