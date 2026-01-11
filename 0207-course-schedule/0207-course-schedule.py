class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # pre - crs
        adj = defaultdict(set)
        for crs, pre in prerequisites:
            adj[crs].add(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                # cycle!
                return False
        
            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adj[crs] = []

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True