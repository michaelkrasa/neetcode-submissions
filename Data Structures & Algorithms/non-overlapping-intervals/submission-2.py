class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Input: intervals = [[1,2],[1,4],[2,4]]
        Output: 1

        overlapping = int2[0] < int1[1]

        --- ---
         ----
        """

        removed = 0
        intervals.sort()
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prevEnd:
                prevEnd = min(prevEnd, end)
                removed += 1
            else:
                prevEnd = end
        return removed