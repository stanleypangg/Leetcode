class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for l, r in intervals[1:]:
            prev_l, prev_r = res[-1]
            if l <= prev_r:
                res[-1][1] = max(prev_r, r)
            else:
                res.append([l, r])
        
        return res