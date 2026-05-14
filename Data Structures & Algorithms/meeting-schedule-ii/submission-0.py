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
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        s, e = 0, 0
        rooms, max_rooms = 0, 0
        
        while s < len(intervals):
            if starts[s] < ends[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            max_rooms = max(rooms, max_rooms)

        return max_rooms
            
