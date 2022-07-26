# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        maxProfit = 0
        minPurchase = prices[0]
        for price in prices:
            curProfit = price - minPurchase
            if curProfit > maxProfit:
                maxProfit = curProfit
            if price < minPurchase:
                minPurchase = price
        return maxProfit

        # naive o(n^2) implementation
        """profit = 0
        for i in range(len(prices)):
            for y in range(i,len(prices)):
                num = prices[y] - prices[i]
                if num > profit:
                    profit = num
        return profit"""
