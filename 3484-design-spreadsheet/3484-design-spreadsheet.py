class Spreadsheet:

    def __init__(self, rows: int):
        self.spreadsheet = {chr(val): [0] * rows for val in range(ord('A'), ord('A') + 26)}

    def _getCell(self, cell: str) -> None:
        col = cell[0]
        row = int(cell[1:])
        return self.spreadsheet[col][row - 1]

    def setCell(self, cell: str, value: int) -> None:
        col = cell[0]
        row = int(cell[1:])
        self.spreadsheet[col][row - 1] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        one, two = formula[1:].split('+')
        total = int(one) if one.isdigit() else self._getCell(one)
        total += int(two) if two.isdigit() else self._getCell(two)
        return total

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)