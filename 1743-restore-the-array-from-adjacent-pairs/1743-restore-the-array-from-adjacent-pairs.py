class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in adjacentPairs:
            adj[u].append(v)
            adj[v].append(u)

        res = []

        source = None
        for node, nei in adj.items():
            if len(nei) == 1:
                source = node
                break

        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            res.append(node)

            for nei in adj[node]:
                dfs(nei)
            
        dfs(source)
        return res