class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        """

        create an empty heap, add a tuple of dist and coordinates
        do it for the whole list
        heapify with function

        """
        heap = []
        for x, y in points:
            dist = x**2 + y**2
            heap.append([dist, x, y])

        heapq.heapify(heap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1

        return res