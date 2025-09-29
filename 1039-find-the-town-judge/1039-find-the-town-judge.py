class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # return town judge if exists
        # trust[i] = [a_i, b_i], a_i trusts b_i

        # directed graph
        # town judge exists if edge to everyone, and everynone has an edge to judge (except themselves)

        adj = {i: [set(), set()] for i in range(1, n + 1)} # label -> [[inbound], [outbound]]
        for a, b in trust:
            adj[a][1].add(b)
            adj[b][0].add(a)
        
        for label in adj:
            inbound, outbound = adj[label]
            if len(inbound) == n - 1 and len(outbound) == 0:
                return label
        
        return -1