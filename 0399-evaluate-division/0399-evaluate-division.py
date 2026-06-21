class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # directed weighted graph
        adj = defaultdict(list)
        for (a, b), value in zip(equations, values):
            adj[a].append((b, value))
            adj[b].append((a, 1 / value))
        
        res = []
        for start, end in queries:
            if start not in adj or end not in adj:
                res.append(-1.0)
                continue

            q = deque([(start, 1.0)])
            visited = set()
            found = False

            while q:
                cur, total = q.popleft()
                if cur == end:
                    res.append(total)
                    found = True
                    break

                if cur in visited:
                    continue
                visited.add(cur)
                
                for nei, weight in adj.get(cur, []):
                    q.append((nei, total * weight))
            
            if not found:
                res.append(-1.0)
        
        return res