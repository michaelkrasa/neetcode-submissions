"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """

        ---
         -
         ----
        (0,2)
        (1,3)
        (1,4)

        two pointers
        starts and ends
        starts < ends
        rooms += 1

        """
        intervals.sort(key=lambda x: x.start)
        minHeap = []
        heapq.heapify(minHeap)

        for interval in intervals:
            if minHeap and interval.start >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, interval.end)

        return len(minHeap)
            
