class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Counter
        counter = Counter(tasks)

        # Max heap of task counter
        heap = []
        for key, value in counter.items():
            heapq.heappush(heap, -value)
        
        time = 0
        q = deque()
        while heap or q:
            if heap:
                task = heapq.heappop(heap) + 1
                if task < 0:
                    q.append((task, time + n + 1))
            time += 1
            
            while q and q[0][1] == time:
                task_count = q.popleft()[0]
                heapq.heappush(heap, task_count)
        
        return time