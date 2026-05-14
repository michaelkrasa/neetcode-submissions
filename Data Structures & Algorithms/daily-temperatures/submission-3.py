class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        brute force - loop through the array
        i, j - go forward through the array and look for a higher value
        save this to the res array when we find it

        [30,38,30,36,35,40,28]
        """
        n = len(temperatures)
        res = [0] * n
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res
        