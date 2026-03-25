class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # O(mn) time, O(m + n) space
        m, n = len(grid), len(grid[0])

        total = 0
        row_sum = [0] * m
        col_sum = [0] * n

        # initial scan
        for r in range(m):
            for c in range(n):
                total += grid[r][c]
                row_sum[r] += grid[r][c]
                col_sum[c] += grid[r][c]
        
        # try all row partitions
        sum1, sum2 = 0, total
        for summ in row_sum:
            sum1 += summ
            sum2 -= summ
            
            if sum1 == sum2:
                return True
        
        # try all col partitions
        sum1, sum2 = 0, total
        for summ in col_sum:
            sum1 += summ
            sum2 -= summ

            if sum1 == sum2:
                return True
        
        return False