'''Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        min_price = float('inf')
        maxprofit = 0
        for p in prices:
            min_price = min(p, min_price)
            max_price = max(p, min_price)
            profit = max_price - min_price
            profits.append(profit)
            maxprofit = max(profits)
        return maxprofit