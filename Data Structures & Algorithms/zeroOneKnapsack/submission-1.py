class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        from functools import cache

        n = len(weight)

        @cache
        def dfs(i: int, remaining: int) -> int:
            if i == n or remaining == 0:
                return 0

            best = dfs(i + 1, remaining)

            wt = weight[i]
            val = profit[i]
            if wt <= remaining:
                best = max(best, val + dfs(i + 1, remaining - wt))

            return best

        return dfs(0, capacity)
