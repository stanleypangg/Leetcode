class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        res = i = 0

        while i < len(cost):
            res += cost[i]
            
            i += 1
            if i >= len(cost):
                break
            res += cost[i]

            i += 2
        
        return res