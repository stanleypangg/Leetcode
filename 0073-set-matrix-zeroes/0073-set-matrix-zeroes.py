class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # O(mn), keey arrays rows and cols, to track which rows and cols need to be zero'd out
        # this is O(mn) space however
        # instead, store this data int he first row and col of the matrix
        # iterate through entire matrix, and mark first row/col
        # this is ok, since the first row/col value would be zero'd out anyways
        # need to process first col/row last to not overwrite information
        # use flags to mark if they are to be zero'd out

        first_col_zeroed = first_row_zeroed = False
        m, n = len(matrix), len(matrix[0])
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                    first_row_zeroed |= r == 0
                    first_col_zeroed |= c == 0
        
        for r in range(1, m):
            if matrix[r][0] == 0:
                matrix[r] = [0] * n
            
        for c in range(1, n):
            if matrix[0][c] == 0:
                for dr in range(m):
                    matrix[dr][c] = 0

        if first_row_zeroed:
            matrix[0] = [0] * n
        
        if first_col_zeroed:
            for dr in range(m):
                matrix[dr][0] = 0