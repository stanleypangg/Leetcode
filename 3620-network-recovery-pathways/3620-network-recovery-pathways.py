class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        # first create adj list
        # u -> (v, weight)

        # run dijkstras
        # keep a best seen 
        # check if k

        n = len(online)
        adj = defaultdict(list)
        max_weight = 0

        for u, v, cost in edges:
            max_weight = max(max_weight, cost)
            adj[u].append((v, cost))

        def traverse(ans):            
            heap = [(0, 0)]
            dist = [float('inf')] * n 
            dist[0] = 0
            
            while heap:
                cost, cur = heapq.heappop(heap)
                if cost > dist[cur]:
                    continue
                    
                if cur == n - 1:
                    return True

                for nei, weight in adj[cur]:
                    if not online[nei] or weight < ans:
                        continue
                    
                    new_cost = cost + weight
                    if new_cost > k or new_cost >= dist[nei]:
                        continue
                    
                    dist[nei] = new_cost
                    heapq.heappush(heap, (new_cost, nei))
            
            return False

        res = -1
        l, r = 0, max_weight
        while l <= r:
            mid = (l + r) // 2
            if traverse(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return res