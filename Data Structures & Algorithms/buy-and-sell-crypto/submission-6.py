class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [r] - [l] = maxProfit
        maxProfit = max(profit, maxProfit)
        """

        maxP, cheapest = 0, prices[0]

        for sell in prices:
            cheapest = min(sell, cheapest)
            maxP = max(sell - cheapest, maxP)
        return maxP
