class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        indeg = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].add(crs)
            indeg[crs] += 1
        
        q = deque([])
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        processed = 0
        while q:
            processed += 1
            u = q.popleft()
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        return processed == numCourses