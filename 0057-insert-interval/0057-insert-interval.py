class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n_start, n_end = newInterval

        def insertMerge(start, end):
            # just insert
            if not res:
                res.append([start, end])
                return

            prev_start, prev_end = res[-1]

            if max(start, prev_start) <= min(end, prev_end):
                res[-1][0] = min(start, prev_start)
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])
        
        for start, end in intervals:
            if res:
                p_start, p_end = res[-1]
            else:
                p_start = p_end = -1
            
            if p_start <= n_start <= end:
                insertMerge(n_start, n_end)
            
            insertMerge(start, end)
        
        if not intervals or n_start > intervals[-1][1]:
            insertMerge(n_start, n_end)

        return res