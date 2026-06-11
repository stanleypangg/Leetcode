class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        def dfs(node, parent):
            max_depth = 0
            for nei in adj[node]:
                if nei != parent:
                    max_depth = max(max_depth, dfs(nei, node) + 1)
            return max_depth
        
        return pow(2, dfs(1, 0) - 1, MOD)