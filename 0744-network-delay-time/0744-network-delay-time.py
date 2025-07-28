class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adjacency list
        adj = defaultdict(list)
        for src, target, time in times:
            adj[src].append((time, target))
        
        # Build distance tracker
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # Initialize heap
        heap = [(0, k)]
        while heap:
            curr_time, u = heapq.heappop(heap)

            # We have already found a shorter path to this node
            if dist[u] < curr_time:
                continue
            
            for travel_time, v in adj[u]:
                if travel_time + dist[u] < dist[v]:
                    dist[v] = dist[u] + travel_time
                    heapq.heappush(heap, (dist[v], v))
        
        max_delay = 0
        for i in range(1, n + 1):
            # Not all nodes have been reached
            if dist[i] == float('inf'):
                return -1
            max_delay = max(max_delay, dist[i])
        
        return max_delay