class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        t, b = 0, m - 1
        while t <= b:
            row = (t + b) // 2
            if target < matrix[row][0]:
                b = row - 1
            elif target > matrix[row][-1]:
                t = row + 1
            else:
                break
        else:
            return False
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False