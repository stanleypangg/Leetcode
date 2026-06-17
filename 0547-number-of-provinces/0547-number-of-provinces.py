class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return
        
        if self.size[rootA] < self.size[rootB]:
            rootA, rootB = rootB, rootA
        
        self.parent[rootB] = rootA
        self.size[rootA] += self.size[rootB]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i, j)
        
        return len({uf.find(i) for i in range(n)})