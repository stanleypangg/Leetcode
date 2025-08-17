class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Suboptimal Solution, fix this
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(node, par):
            if visited[node]:
                return True # node has been visited
            
            visited[node] = True # set current node to visited

            # Iterate over neighbours
            for nei in adj[node]:
                if nei == par:
                    continue # skip the immediate parent
                elif dfs(nei, node): # recurse into neighbour
                    return True 
            
            return False

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = [False] * (n + 1)

            if dfs(u, -1):
                return [u, v]