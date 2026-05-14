class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        this is is a lot like two sum with two pointers
        iterate through the list and look for a combination of numers
        which adds up to its negative
        """

        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            # bin search
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append((num, nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
