class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        nei = [0] * n
        for u, v in roads:
            nei[u] += 1
            nei[v] += 1
            
        nei.sort()
        return sum(nei[i - 1] * i for i in range(1, n + 1))