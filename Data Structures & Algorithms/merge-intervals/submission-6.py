class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]

        # [[1,3],[1,5],[6,7]]
        # [[1,3] []
        # ---
        #  ----

        for start, end in intervals:
            if res[-1][1] >= start:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])

        return res
        