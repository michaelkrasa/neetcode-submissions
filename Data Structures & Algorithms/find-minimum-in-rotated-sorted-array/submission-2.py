class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        ascedning order tells me binary search

        [biggest number, smallest number]

        [2,3,4,5,6,1]
        [3, 4, 5, 6, 1, 2, 3]
        l           l   m   r
        """
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # looking for the correct array
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(nums[m], res)
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1

        return res

        

        
        