class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        same as regular kadanes algorithm
        - still keep track of the largest subarray sum
        - but also keep track of smallest subarray sum
        
        depending on which is larger - largest subarray sum or
        total minus smallest subarray sum = for the loop around
        """ 
        globMax, globMin = nums[0], nums[0]
        curMax, curMin, total = 0, 0, 0

        for num in nums:
            total += num
            curMax = max(num + curMax, num)
            curMin = min(num + curMin, num)
            globMax = max(globMax, curMax)
            globMin = min(globMin, curMin)

        return max(globMax, total - globMin) if globMax > 0 else globMax