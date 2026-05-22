class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        rows = [[] for _ in range(numRows)]
        idx = 0
        phase = 1

        for c in s:
            rows[idx].append(c)

            if idx == 0:
                phase = 1
            elif idx == numRows - 1:
                phase = -1
            
            idx += phase
        
        return ''.join(''.join(row) for row in rows)