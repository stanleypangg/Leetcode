class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.hashset = set()
        self.q = deque()
        self.dest = defaultdict(deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.hashset:
            return False

        if len(self.q) == self.limit:
            self.forwardPacket()
        
        self.q.append(packet)
        self.hashset.add(packet)
        self.dest[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.q) == 0:
            return []
        
        packet = self.q.popleft()
        self.hashset.remove(packet)
        self.dest[packet[1]].popleft()
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        time = self.dest[destination]

        l, r = 0, len(time) - 1
        while l <= r:
            mid = (l + r) // 2
            if time[mid] < startTime:
                l = mid + 1
            else:
                r = mid - 1
        
        left = l
        
        l, r = 0, len(time) - 1
        while l <= r:
            mid = (l + r) // 2
            if time[mid] > endTime:
                r = mid - 1
            else:
                l = mid + 1
        
        return r - left + 1


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)