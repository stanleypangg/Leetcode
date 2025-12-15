class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # detect cycle and connectiveness
        if len(edges) != n - 1:
            # trees have n - 1 vertices
            return False
        
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        visited = set()
        
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in adj[node]:
                if neighbor == prev:
                    continue
                
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        if not dfs(0, -1):
            return False
        
        return len(visited) == n