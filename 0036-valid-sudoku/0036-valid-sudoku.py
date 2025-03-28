class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(9)]
        col_check = [set() for _ in range(9)]
        box_check = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == '.':
                    continue

                if curr in row_check[i]:
                    return False
                row_check[i].add(curr)

                if curr in col_check[j]:
                    return False
                col_check[j].add(curr)

                if curr in box_check[i // 3][j // 3]:
                    return False
                box_check[i // 3][j // 3].add(curr)
        
        return True