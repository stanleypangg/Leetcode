class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def add(r, c):
            cur = board[r][c]
            rows[r].add(cur)
            cols[c].add(cur)
            boxes[r // 3][c // 3].add(cur)

        def remove(r, c):
            cur = board[r][c]
            rows[r].remove(cur)
            cols[c].remove(cur)
            boxes[r // 3][c // 3].remove(cur)

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    add(r, c)
        
        def bt(i):
            if i >= len(empty):
                return True
            
            r, c = empty[i]
            valid = {n for n in '123456789'} - rows[r] - cols[c] - boxes[r // 3][c // 3]

            for num in valid:
                board[r][c] = num
                add(r, c)
                if bt(i + 1):
                    return True
                remove(r, c)
            
            return False
        
        bt(0)
