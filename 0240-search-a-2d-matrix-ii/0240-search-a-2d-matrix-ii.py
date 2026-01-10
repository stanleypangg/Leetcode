class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # sorted left to right in ascending
        # sorted ascending from top to bottom
        # binary search this hoe
        
        # brute force is O(mn)
        # binary search each row and col is O(nlogm + mlogn)

        # we could also just do every single row/col
        # this could be O(mlogn) or O(nlogm)
        # pick the smaller m or n as the linear value

        if m < n:
            for row in matrix:
                l, r = 0, n - 1
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
        else:
            for col in range(n):
                l, r = 0, m - 1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[mid][col] == target:
                        return True
                    elif matrix[mid][col] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
        
        return False