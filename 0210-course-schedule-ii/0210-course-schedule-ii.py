class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indeg[crs] += 1

        q = deque([])
        for crs in range(numCourses):
            if indeg[crs] == 0:
                q.append(crs)
        
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        if len(res) != numCourses:
            return []
        return res