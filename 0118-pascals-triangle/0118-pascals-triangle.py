class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []

        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    above = ret[i - 1]
                    row.append(above[j - 1] + above[j])
            ret.append(row)

        return ret