class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        top = left = 0
        bottom = right = n - 1

        while top <= bottom and left <= right:
            for i in range(left, right):
                temp, matrix[top][i] = matrix[top][i], matrix[n - 1 - i][left]
                temp, matrix[i][right] = matrix[i][right], temp
                temp, matrix[bottom][n - 1 - i] = matrix[bottom][n - 1 - i], temp
                matrix[n - 1 - i][left] = temp

            left += 1
            right -= 1
            top += 1
            bottom -= 1