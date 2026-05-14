class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        import functools
        @functools.cache
        def dfs(i):
            if i >= n:
                return 0
            return max(dfs(i + 1), nums[i] + dfs(i + 2))
        
        return dfs(0)
