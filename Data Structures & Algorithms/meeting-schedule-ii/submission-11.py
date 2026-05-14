"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # have a heap -- why?
        # heap size will be num of rooms being used at a time

        intervals.sort(key=lambda k:k.start)
        heap = []

        for i in intervals:
            if heap and heap[0] <= i.start:
                # we can evict the room and reuse it
                heapq.heappop(heap)
            heapq.heappush(heap, i.end)
        return len(heap)