class Solution:
    def top_sort(self, k, conditions):
        indeg = [0] * (k + 1)
        graph = [[] for _ in range(k + 1)]
        for node, nei in conditions:
            graph[node].append(nei)
            indeg[nei] += 1
        
        count = 0
        order = {}
        q = deque(i for i in range(1, k + 1) if indeg[i] == 0)

        while q:
            node = q.popleft()
            order[node] = count
            count += 1

            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        if count + 1 != len(graph):
            return []
        return order

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = self.top_sort(k, rowConditions)
        print(row_order)
        if not row_order:
            return [] 

        col_order = self.top_sort(k, colConditions)
        if not col_order:
            return []
        
        res = [[0] * k for _ in range(k)]
        for i in range(1, k + 1):
            r, c = row_order[i], col_order[i]
            res[r][c] = i
        
        return res
