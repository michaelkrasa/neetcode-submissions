class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        non-overlapping
        [start, end]
        ascending order start

        end_i < start_i+1


        happy path:
        start is after end of previous

        end is before start of next
        - else end = end of next

        [[1,3],[4,6]], newInterval = [2,5]


        """
        start, end = newInterval
        i, n = 0, len(intervals)
        res = []

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res