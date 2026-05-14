class Solution:
    def permute(self, nums):
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums, idx):

        # BASE CASE
        if idx == len(nums):
            self.res.append(nums.copy())
            return

        # TRY ALL SWAPS
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx + 1)
            nums[idx], nums[i] = nums[i], nums[idx]


# [1,2,3] [1,3,2]
# [2,1,3] [2,3,1]
# [3,2,1] [3,1,2]