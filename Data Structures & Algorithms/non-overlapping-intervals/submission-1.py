class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Input: intervals = [[1,2],[1,4],[2,4]]
        Output: 1

        overlapping = int2[0] < int1[1]

        ---
          ---
           ----
        """
        intervals.sort()
        erased = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if prevEnd > start:
                erased += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end

        return erased