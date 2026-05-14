class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS
        """
        [2,4,1,1,1,1]
             -   -

        """

        l = r = res = 0
        n = len(nums)

        while r < n - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, nums[i] + i)
            l = r + 1
            r = farthest
            res += 1
        
        return res