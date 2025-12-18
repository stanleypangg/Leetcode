class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            for i in range(right - left):
                temp, matrix[top][left + i] = matrix[top][left + i], matrix[bottom - i][left]
                temp, matrix[top + i][right] = matrix[top + i][right], temp
                temp, matrix[bottom][right - i] = matrix[bottom][right - i], temp
                matrix[bottom - i][left] = temp

            left += 1
            right -= 1
            top += 1
            bottom -= 1