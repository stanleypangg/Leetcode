class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_idx = 0
        self.score = 0
        self.body = {(0, 0)}
        self.q = deque([(0, 0)])

    def move(self, direction: str) -> int:
        dirs = {
            'R': (0, 1),
            'D': (1, 0),
            'U': (-1, 0),
            'L': (0, -1)
        }

        dr, dc = dirs[direction]

        head_r, head_c = self.q[-1]
        next_r, next_c = head_r + dr, head_c + dc

        if next_r < 0 or next_r >= self.height or next_c < 0 or next_c >= self.width:
            return -1
        
        eating = (
            self.food_idx < len(self.food) and
            [next_r, next_c] == self.food[self.food_idx]
        )

        tail = self.q[0]
        if (next_r, next_c) in self.body and (eating or (next_r, next_c) != tail):
            return -1

        if eating:
            self.score += 1
            self.food_idx += 1
        else:
            tail_r, tail_c = self.q.popleft()
            self.body.remove((tail_r, tail_c))

        self.q.append((next_r, next_c))
        self.body.add((next_r, next_c))
        
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)