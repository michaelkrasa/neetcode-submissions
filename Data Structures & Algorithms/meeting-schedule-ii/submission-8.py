"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap = []                # end times of active meetings
        max_rooms = 0

        for it in intervals:
            # free up all rooms that have finished
            while heap and it.start >= heap[0]:
                heapq.heappop(heap)

            # occupy a room with current meeting
            heapq.heappush(heap, it.end)

            # track the peak number of rooms in use
            max_rooms = max(max_rooms, len(heap))

        return max_rooms