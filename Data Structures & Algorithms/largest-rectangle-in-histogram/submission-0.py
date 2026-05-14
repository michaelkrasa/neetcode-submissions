class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        best = 0
        stack = [-1]

        for i, h in enumerate(heights + [0]):
            while stack[-1] != -1 and h < heights[stack[-1]]:
                # width, height, calculate best area
                height = heights[stack.pop()] # left
                left = stack[-1]
                width = i - left - 1
                best = max(best, height * width)
            stack.append(i)

        return best