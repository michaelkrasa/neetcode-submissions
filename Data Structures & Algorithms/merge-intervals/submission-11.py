class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        """
        Input: intervals = [[1,3],[1,5],[6,7]]
        Output: [[1,5],[6,7]]
        """
        
        intervals.sort()
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= output[-1][1]: # overlap -> merge
                output[-1][1] = max(end, output[-1][1])
            else:
                output.append([start, end])
        return output