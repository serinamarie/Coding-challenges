# Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

# The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

# Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # input: array
        # output: int
        # constraints: n is even, n is at least 2, n is the length of the array, input array could be made up of very large values or large negative values
        
        # ex. candyType = [1,1,2,2,3,3]
        # output: 3
        
        # get the length of the input
        num_candies = len(candyType)
        
        # divide the length by 2
        doctors_orders = int(num_candies/2)
                
        # return the min of either doctors_orders or the max variety
        return min(len(set(candyType)), doctors_orders)
        
 
    

    
