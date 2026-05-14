class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        this is is a lot like two sum with two pointers
        iterate through the list and look for a combination of numers
        which adds up to its negative

        """
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i - 1] == n:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = n + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1

        return res

            
            