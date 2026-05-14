class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == 0: 
            return []
        freq = Counter(nums)
        heap = []  # min-heap of (count, value)
        for val, cnt in freq.items():
            heapq.heappush(heap, (cnt, val))
            if len(heap) > k:
                heapq.heappop(heap)
        return [val for _, val in heap]
        