class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        res = 0
        visited = set()

        for i in range(n):
            if i in visited:
                continue
            
            q = deque([i])
            nodes = {i}
            visited.add(i)

            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if nei not in nodes:
                        q.append(nei)
                        nodes.add(nei)
                        visited.add(nei)

            connected = True
            for j in nodes:
                if len(adj[j]) != len(nodes) - 1:
                    connected = False
                    break

            if connected == True:
                res += 1
    
        return res