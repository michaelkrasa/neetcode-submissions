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
        
        for i in range(n):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                j += 1
            if j < n:
                res[i] = j - i

        return res
        