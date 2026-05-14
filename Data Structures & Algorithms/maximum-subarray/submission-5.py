class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algo
        # if prev sum is smaller than num at index, disregard it
        best = curSum = nums[0]

        for num in nums[1:]:
            curSum = max(num, curSum + num)
            best = max(best, curSum)
        return best