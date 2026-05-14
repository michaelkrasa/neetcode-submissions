import functools

class Solution:
    def climbStairs(self, n: int) -> int:

        @functools.cache
        def dfs(i):
            if i >= n:
                return i == n
            return dfs(i + 1) + dfs(i + 2)

        return dfs(0)