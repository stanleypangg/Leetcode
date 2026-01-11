class TicTacToe:
    # n x n board
    # 2 players
    # move is valid if placed on empty block
    # once win condition is reached, no more moves allowed
    # player who succeeds in placing n of their marks in a horizontal vertical or diagnoal row wins

    def __init__(self, n: int):
        self.n = n

        # since each move is guaranteed to be valid -> block is always empty before move
        # we do not need which individual block is empty or not
        # track win condition of the counts
        # also need to differentiate by player
        # differentiate by player by using player to key their counts

        # rows and cols are easy
        self.rows = {1: [0] * n, 2: [0] * n}
        self.cols = {1: [0] * n, 2: [0] * n}

        # diagonals, we have two
        # top left to bottom right -> diagonal 1
        # bottom left to top right -> diagonal 2
        
        # if row == col, we are part of diagonal 1
        # if row == n - col, we are part of diagonal 2

        self.diagonal = {1: [0, 0], 2: [0, 0]}

    def move(self, row: int, col: int, player: int) -> int:
        # player with id player plays at cell (row, col)
        # move is guaranteed to be valid
        # return: 0 if no winner
        # 1 if player 1 wins
        # 2 if player 2 wins
        
        self.rows[player][row] += 1
        if self.rows[player][row] == self.n:
            return player
        
        self.cols[player][col] += 1
        if self.cols[player][col] == self.n:
            return player

        if row == col:
            self.diagonal[player][0] += 1
            if self.diagonal[player][0] == self.n:
                return player
        
        if row == self.n - col - 1:
            self.diagonal[player][1] += 1
            if self.diagonal[player][1] == self.n:
                return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)