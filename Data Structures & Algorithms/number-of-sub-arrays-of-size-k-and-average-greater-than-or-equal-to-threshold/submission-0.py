class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curSum = sum(arr[:k])

        res = 1 if curSum / k >= threshold else 0

        for i in range(k, len(arr)):
            curSum += arr[i] - arr[i - k]
            if curSum / k >= threshold:
                res += 1

        return res
            

        