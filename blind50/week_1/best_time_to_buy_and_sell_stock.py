# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock. Return the maximum profit you can achieve 
# from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # constraints: single day < different day in the future
        # output: 0 if no profit, else max profit
        # input: list of length 1 or higher. items in list will be at least 0
        # edge cases: if list is length 1 return 0
        # plan:
        # iterative: buy on day 1, try to sell
            # scenario 1: price is lower or same, then pass
            # scenario 2: price is higher, see if profit is better than best_profit
                # if profit would be better than best profit, set new best_profit
                # else: pass
        # buy on day 2... repeat process
        
#         best_profit = 0
#         buy_day = 0
        
#         while buy_day < len(prices)-1:
#             buy_price = prices[buy_day]
    
#             for i in range(buy_day+1, len(prices)):
#                 current_price = prices[i]
#                 if current_price > buy_price:
#                     profit = current_price - buy_price
#                     if profit > best_profit:
#                         best_profit = profit
        
#             buy_day += 1
                    
                       
#         return best_profit

        # what is lower, day 0 value or current value
        # what is higher, profit of 0 or this profit?
        
        best_profit = 0
        lowest_price = prices[0] 
        for price in prices:
            lowest_price = min(price, lowest_price) 
            best_profit = max(price-lowest_price, best_profit)
            
        return best_profit