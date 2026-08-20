class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        prev = costs[0]

        for i in range(1, n):
            min1, min2, min1_idx = float('inf'), float('inf'), -1
            for j, cost in enumerate(prev):
                if cost < min1:
                    min1, min2, min1_idx = cost, min1, j
                elif cost < min2:
                    min2 = cost
                
            cur = [0] * k
            for j in range(k):
                prev_min = min1 if j != min1_idx else min2
                cur[j] = prev_min + costs[i][j]
            
            prev = cur
        
        return min(prev)
                    