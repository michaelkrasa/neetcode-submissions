class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # calculate frequency of numbers in list
        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        # save to array so we can sort it
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            num = heapq.heappop(heap)[1]
            res.append(num)
                
        return res
        