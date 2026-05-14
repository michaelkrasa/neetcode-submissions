class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = curr = nums[0]
        for x in nums[1:]:
            curr = max(x, curr + x)  # dp step
            best = max(best, curr)   # track global max
        return best