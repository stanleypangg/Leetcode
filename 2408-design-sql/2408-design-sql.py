class Table:
    def __init__(self, arity):
        self.serial = 1
        self.arity = arity
        self.rows = {}

class SQL:

    def __init__(self, names: list[str], columns: list[int]):
        # n tables
        # names[i] = table names
        # columns[i] = # of columns
        self.tables = {
            name: Table(column) # name -> (id, arity, rows)
            for name, column
            in zip(names, columns)
        }

    def ins(self, name: str, row: list[str]) -> bool:
        table = self.tables.get(name)
        if table is None or len(row) != table.arity:
            return False
        
        rowId = table.serial
        table.rows[rowId] = row
        table.serial += 1
        return True

    def rmv(self, name: str, rowId: int) -> None:
        table = self.tables.get(name)
        if table is None or rowId not in table.rows:
            return
        del table.rows[rowId]

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        table = self.tables.get(name)
        idx = columnId - 1
        if (
            table is None
            or rowId not in table.rows
            or idx >= len(table.rows[rowId])
        ):
            return '<null>'
        
        row = table.rows[rowId]
        return row[idx]

    def exp(self, name: str) -> list[str]:
        table = self.tables.get(name)
        if table is None:
            return []
        
        return [
            ','.join([str(rowId)] + row) 
            for rowId, row
            in table.rows.items()
        ]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)