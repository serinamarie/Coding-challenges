# Say you have an array prices for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # output: max profit as int
        # input: array of stock prices
        # constraints: length of input array is 1 to 3*10**4, input values could be 0 or up to 10**4
        # edge cases: input array of length 1, or 2, values of 0
        
        # account for peaks and valleys, and also if we reach the end of the list
        
        # store profit within wallet variable as 0
        wallet = 0
        
        # iterate through stock prices
        for i in range(len(prices)-1):
            
            # choose the max of either 0 or if the (next value - the current one) is greater than 0
            wallet += max(prices[i+1] - prices[i], 0)
        
        return wallet