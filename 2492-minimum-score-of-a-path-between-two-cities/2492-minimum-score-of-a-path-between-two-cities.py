class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))
        
        min_score = float('inf')
        visited = {1}
        q = deque([1])
        while q:
            cur = q.popleft()
            for nei, d in adj[cur]:
                min_score = min(min_score, d)

                if nei in visited:
                    continue
                
                visited.add(nei)
                q.append(nei)
        
        return min_score