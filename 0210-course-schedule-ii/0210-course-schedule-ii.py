class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited = set()
        path = set()
        res = []
        def dfs(crs):
            if crs in visited:
                return True
            if crs in path:
                return False
            
            path.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)

            visited.add(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res