class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        pos = {}
        m, n = len(mat), len(mat[0])
        row_counts = [0] * m
        col_counts = [0] * n

        # scan mat for all locations
        for r in range(m):
            for c in range(n):
                cur = mat[r][c]
                pos[cur] = (r, c)
        
        for i in range(len(arr)):
            r, c = pos[arr[i]]

            row_counts[r] += 1
            if row_counts[r] == n:
                return i
            
            col_counts[c] += 1
            if col_counts[c] == m:
                return i