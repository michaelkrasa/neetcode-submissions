class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        non-overlapping
        [start, end]
        ascending order start
        intervals=[[1,3],[4,6]]
       newInterval=.[2,    5]
        """
        i, n = 0, len(intervals)
        result = []

        # 1️⃣ Add all intervals before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        result.append(newInterval)

        return result + intervals[i:]