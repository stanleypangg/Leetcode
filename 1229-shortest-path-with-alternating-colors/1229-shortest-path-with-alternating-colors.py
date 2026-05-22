class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        adj_red = {}
        for a, b in redEdges:
            if a not in adj_red:
                adj_red[a] = []
            adj_red[a].append(b)
        
        adj_blue = {}
        for u, v in blueEdges:
            if u not in adj_blue:
                adj_blue[u] = []
            adj_blue[u].append(v)

        res = [-1] * n
        q = deque([(0, 0, 1), (0, 0, -1)])
        visited = {(0, 1), (0, -1)} # node, colour

        while q:
            node, length, colour = q.popleft()
            if res[node] == -1:
                res[node] = length
            else:
                res[node] = min(res[node], length)

            next_adj = adj_red if colour == -1 else adj_blue
            for nei in next_adj.get(node, []):
                if (nei, colour * -1) in visited:
                    continue
                q.append((nei, length + 1, colour * -1))
                visited.add((nei, colour * -1))
        
        return res