class Solution:
    def minimumCost(self, n: int, highways: list[list[int]], discounts: int) -> int:
        # build adj list
        adj = defaultdict(list)
        for c1, c2, toll in highways:
            adj[c1].append((c2, toll))
            adj[c2].append((c1, toll))

        # dist[node][discount] = min distance at node with discount used
        dist = [[float('inf')] * (discounts + 1) for _ in range(n)]
        dist[0][0] = 0 # start node
        
        # (cost, node, discounts used)
        heap = []
        heapq.heappush(heap, (0, 0, 0))

        while heap:
            cost, node, discounts_used = heapq.heappop(heap)
            if node == n - 1:
                return cost

            for nei, toll in adj[node]:
                # traverse w/o discount
                if dist[nei][discounts_used] > cost + toll:
                    dist[nei][discounts_used] = cost + toll
                    heapq.heappush(heap, (cost + toll, nei, discounts_used))

                if discounts_used < discounts and dist[nei][discounts_used + 1] > cost + toll // 2:
                    dist[nei][discounts_used + 1] = cost + toll // 2
                    heapq.heappush(heap, (cost + toll // 2, nei, discounts_used + 1))
        
        return -1