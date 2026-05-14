class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums_set = set()

        for _, num in enumerate(nums):
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False

        