class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        cases:
            1. non zero numbers - multiply all and safe divide into each
            2. one zero - everything is 0 except for the 0 where its product
            3. more than one zero - everything is 0
        """

        zeros = nums.count(0)
        if zeros > 1:
            return [0] * len(nums)

        total = 1
        for n in nums:
            if n != 0:
                total *= n

        if zeros == 0:
            return [total // n for n in nums]
        else:  # exactly one zero
            return [total if n == 0 else 0 for n in nums]