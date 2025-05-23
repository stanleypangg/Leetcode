class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = set()
        self.pre_map = defaultdict(set)

        for course, pre in prerequisites:
            self.pre_map[course].add(pre)

        def dfs(course):
            if course in self.visited:
                return False

            pre_set = self.pre_map[course]
            if not pre_set:
                return True

            self.visited.add(course)
            for pre in pre_set:
                if not dfs(pre):
                    return False
            self.visited.remove(course)
            self.pre_map[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True