class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
        
        res = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            res += 1
        
        return res