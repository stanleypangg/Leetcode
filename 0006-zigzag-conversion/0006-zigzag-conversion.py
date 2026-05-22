class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        idx = 0
        phase = 1

        for c in s:
            rows[idx] += c
            if idx == 0:
                phase = 1
            elif idx == numRows - 1:
                phase = -1
            idx += phase
        
        return ''.join(rows)