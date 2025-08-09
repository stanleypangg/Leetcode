class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)]) # sorts enqueue -> processing time -> index
        i = 0
        heap = []
        time = tasks[0][0]
        while len(res) < len(tasks):
            # add queuable processes
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if heap:
                process_time, index = heapq.heappop(heap)
                time += process_time
                res.append(index)
            elif i < len(tasks):
                time = tasks[i][0]
        return res