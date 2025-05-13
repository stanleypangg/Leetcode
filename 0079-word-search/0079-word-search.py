class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            elif not (0 <= r < m and 0 <= c < n) or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            found = (
                dfs(r + 1, c, i + 1) or 
                dfs(r - 1, c, i + 1) or 
                dfs(r, c + 1, i + 1) or 
                dfs(r, c - 1, i + 1) 
            )
            board[r][c] = temp

            return found
    
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False