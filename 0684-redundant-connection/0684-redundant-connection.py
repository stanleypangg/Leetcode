class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) # Tree has n - 1 edges, this problem + 1 edge, thus # of edges = # of vertices
        par = [i for i in range(n + 1)]

        def find(n):
            while par[n] != n:
                par[n] = par[par[n]]
                n = par[n]
            return n
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1 == p2:
                return False
            par[p2] = p1
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        