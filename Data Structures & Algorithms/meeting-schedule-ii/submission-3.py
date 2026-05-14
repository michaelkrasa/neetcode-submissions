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
        min_heap = []
        heapq.heapify(min_heap)

        for interval in intervals:
            if min_heap and interval.start >= min_heap[0]:
                heapq.heappop(min_heap)    
            
            heapq.heappush(min_heap, interval.end)
        

        return len(min_heap)
            
