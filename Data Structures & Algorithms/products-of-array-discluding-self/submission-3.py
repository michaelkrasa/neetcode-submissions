class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        cases:
            1. non zero numbers - multiply all and safe divide into each
            2. one zero - everything is 0 except for the 0 where its product
            3. more than one zero - everything is 0
        """


        product, zero_count = 1, 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)

        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if zero_count == 0:
                res[i] = product // num
            else:
                if num == 0:
                    res[i] = product
                else:
                    res[i] = 0

        return res