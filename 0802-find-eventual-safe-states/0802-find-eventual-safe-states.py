class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [0] * n

        def dfs(i):
            if state[i] == 1:
                return False
            elif state[i] == 2:
                return True
            
            state[i] = 1

            for nei in graph[i]:
                if not dfs(nei):
                    return False
            
            state[i] = 2
            return True
        
        return [i for i in range(n) if dfs(i)]
