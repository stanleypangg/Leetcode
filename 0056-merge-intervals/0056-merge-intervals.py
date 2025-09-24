class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn): sort intervals, then just find overlap
        res = []
        intervals.sort()
        curr_s, curr_e = intervals[0]
        for start, end in intervals:
            if curr_s <= start <= curr_e:
                curr_e = max(curr_e, end)
            else:
                res.append([curr_s, curr_e])
                curr_s, curr_e = start, end
        if not res or res[-1] != [curr_s, curr_e]:
            res.append([curr_s, curr_e])
        return res