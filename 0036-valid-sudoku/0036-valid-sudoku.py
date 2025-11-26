class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Data structures to track duplicates in row, col, box
        row_store = [set() for _ in range(9)]
        col_store = [set() for _ in range(9)]
        box_store = [[set() for _ in range(3)] for _ in range(3)]

        # Main loop
        for r in range(9):
            for c in range(9):
                # do something with board[i][j]
                curr = board[r][c]

                if curr == ".":
                    continue

                if curr in row_store[r] or curr in col_store[c] or curr in box_store[r // 3][c // 3]:
                    return False
                
                row_store[r].add(curr)
                col_store[c].add(curr)
                box_store[r // 3][c // 3].add(curr)
        
        return True