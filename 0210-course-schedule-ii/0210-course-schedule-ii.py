class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []

        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        def dfs(crs):
            if state[crs] == 1:
                return False # cycle!
            if state[crs] == 2:
                return True # we are already done with this
            
            # set current to visiting
            state[crs] = 1
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            state[crs] = 2
            res.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res