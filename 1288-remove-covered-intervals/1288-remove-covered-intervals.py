class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        removed = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))

        removed = max_end = 0

        for start, end in intervals:
            if end <= max_end:
                removed += 1
            else:
                max_end = end
        
        return n - removed