class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.score = 0
        self.q = deque([(0, 0)])
        self.body = {(0, 0)}
        self.food_index = 0
        self.food = food

    def move(self, direction: str) -> int:
        dirs = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
        dr, dc = dirs[direction]

        r, c = self.q[-1] # top of queue is the head
        nr, nc = r + dr, c + dc

        # wall collision
        if nr < 0 or nr >= self.height or nc < 0 or nc >= self.width:
            return -1

        eating = (
            self.food_index < len(self.food) and
            nr == self.food[self.food_index][0] and
            nc == self.food[self.food_index][1]
        )

        # self collision
        tail = self.q[0]
        if (nr, nc) in self.body and (eating or (nr, nc) != tail):
            return -1

        if eating:
            self.score += 1
            self.food_index += 1
        else:
            tr, tc = self.q.popleft()
            self.body.remove((tr, tc))
        
        self.q.append((nr, nc))
        self.body.add((nr, nc))

        return self.score
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)