class HitCounter:

    def __init__(self):
        self.counter = [[0, t] for t in range(1, 301)]

    def hit(self, timestamp: int) -> None:
        index = (timestamp - 1) % 300
        _, bucket_timestamp = self.counter[index]
        
        if bucket_timestamp != timestamp:
            self.counter[index] = [0, timestamp]
        self.counter[index][0] += 1

    def getHits(self, timestamp: int) -> int:
        return sum(
            count for count, bucket_timestamp in self.counter
            if timestamp - 300 < bucket_timestamp
        )


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)