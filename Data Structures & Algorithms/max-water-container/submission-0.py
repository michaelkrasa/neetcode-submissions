class Solution:
    def maxArea(self, heights: List[int]) -> int:

        """

        two pointer problem

        if left bar is smaller then the right, increment

        if right is smaller then left, decrement
        
        once we find balance calculate the volume by taking the shorter one
        and multiply is by distance between two two of them

        """

        max_v = 0
        l, r = 0, len(heights) - 1
        while l < r:
            smaller_wall = min(heights[l], heights[r])
            max_v = max(max_v, (r - l) * smaller_wall)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_v
        