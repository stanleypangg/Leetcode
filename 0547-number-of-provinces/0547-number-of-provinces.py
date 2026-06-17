class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        res = 0
        visited = [False] * n

        def dfs(i):
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] and not visited[j]:
                    dfs(j)
            
        for i in range(n):
            if not visited[i]:
                res += 1
                dfs(i)
        
        return res