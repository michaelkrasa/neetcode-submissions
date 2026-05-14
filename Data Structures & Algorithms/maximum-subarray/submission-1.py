class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]

        curSum, maxSum = dp[0], dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i-1] + nums[i])
        return max(dp)