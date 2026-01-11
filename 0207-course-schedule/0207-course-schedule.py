class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # pre - crs
        adj = defaultdict(set)
        for crs, pre in prerequisites:
            adj[crs].add(pre)
        
        visited = set()
        path = set()
        def dfs(crs):
            if crs in visited:
                return True
            if crs in path:
                # cycle!
                return False
        
            path.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            visited.add(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True