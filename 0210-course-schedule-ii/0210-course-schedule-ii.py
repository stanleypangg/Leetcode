class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[pre].append(crs)
        
        res = [0] * numCourses
        self.i = numCourses - 1

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def dfs(crs):
            if state[crs] == 1:
                return False
            if state[crs] == 2:
                return True
            
            state[crs] = 1
            for neighbour in adj[crs]:
                if not dfs(neighbour):
                    return False
            state[crs] = 2
            res[self.i] = crs
            self.i -= 1
        
            return True
        
        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return []
        
        return res