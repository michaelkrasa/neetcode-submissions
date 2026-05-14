class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for p in prices:
            minPrice = min(p, minPrice)
            maxProfit = max(p - minPrice, maxProfit)

        return maxProfit