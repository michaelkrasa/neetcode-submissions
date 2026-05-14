class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        counter = Counter(nums)
        """
        1: 1
        2: 2
        3: 3
        """
        freq = [[] for i in range(len(nums) + 1)]
        # bucket sort - key is frequency, val is num
        for num, cnt in counter.items():
            freq[cnt].append(num)

        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []
        