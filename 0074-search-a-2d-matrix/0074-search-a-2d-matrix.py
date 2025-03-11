class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2
            mid_row = mid // m
            mid_col = mid % m
            mid_val = matrix[mid_row][mid_col]

            if target == mid_val:
                return True
            elif target < mid_val:
                r = mid - 1
            else:
                l = mid + 1
        
        return False