class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        cur = costs[0]

        for i in range(1, n):
            prev = cur
            cur = [float('inf')] * k

            for colour in range(k):
                for other in range(k):
                    if colour == other:
                        continue
                    
                    cur[colour] = min(cur[colour], prev[other] + costs[i][colour])
        
        return min(cur)
                    