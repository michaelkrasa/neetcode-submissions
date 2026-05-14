class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        r - l = maxProfit
        maxProfit = max(profit, maxProfit)

        """
        
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(sell, minBuy)

        return maxP
