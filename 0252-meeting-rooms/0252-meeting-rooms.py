class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if 0 <= len(intervals) <= 1:
            return True

        intervals.sort()
        for i, (start, end) in enumerate(intervals[1:], start=1):
            if start < intervals[i - 1][1]:
                return False
        
        return True