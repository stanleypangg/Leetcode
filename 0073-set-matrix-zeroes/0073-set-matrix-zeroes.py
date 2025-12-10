class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # loop over every element
        # if 0 encountered, we can just mark its rows and cols to placeholder
        # if another 0 encoutnered in this process, we can just ignore it, since we 
        # need to differentiate between a new zero and an original zero
        # once finished, pass over the entire matrix again and change all the placeholders to zero

        m, n = len(matrix), len(matrix[0])
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    for dr in range(m):
                        if matrix[dr][c] == 0:
                            continue
                        matrix[dr][c] = '*'
                    for dc in range(n):
                        if matrix[r][dc] == 0:
                            continue
                        matrix[r][dc] = '*'
                    matrix[r][c] = '*'
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '*':
                    matrix[r][c] = 0