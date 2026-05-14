class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        # [2,10,10,30,30,30]
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]: # new unique value -- save
                # where to put it? at index L
                nums[l] = nums[r]
                l += 1
        return l



