class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]

        maxSum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i-1] + nums[i])
            maxSum = max(maxSum, dp[i])
        return maxSum