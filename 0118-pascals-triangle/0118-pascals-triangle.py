class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]

        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                above = ret[i - 1]
                row.append(above[j - 1] + above[j])
            row.append(1)
            ret.append(row)

        return ret