class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        lmax = rmax = water = 0
        l, r = 0, len(height) - 1
        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            if lmax < rmax:
                water += lmax - height[l]
                l += 1
            else:
                water += rmax - height[r]
                r -= 1
        return water
