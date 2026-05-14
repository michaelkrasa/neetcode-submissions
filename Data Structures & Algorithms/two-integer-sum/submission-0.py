class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # save the pair to a dict
        # k:number, v:index
        diffs = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffs:
                return [diffs[diff], i]
            else:
                diffs[num] = i

        return False
        