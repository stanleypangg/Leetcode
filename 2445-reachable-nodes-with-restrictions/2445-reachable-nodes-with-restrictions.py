class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)

        adj = defaultdict(set)
        for u, v in edges:
            if u not in restricted and v not in restricted:
                adj[u].add(v)
                adj[v].add(u)

        self.res = 1
        
        def dfs(curr, prev):
            for neighbour in adj[curr]:
                if neighbour == prev:
                    continue
                self.res += 1
                dfs(neighbour, curr)
        
        dfs(0, -1)
        return self.res