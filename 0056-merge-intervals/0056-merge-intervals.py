class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn): sort intervals, then just find overlap
        res = []
        intervals.sort()
        
        for interval in intervals:
            # if res is empty or most recent end doesn't overlap next start
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # overlap, externd end of furthest one
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res