class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        red, green, blue = costs[0]

        for i in range(1, n):
            n_red = min(green, blue) + costs[i][0]
            n_green = min(red, blue) + costs[i][1]
            n_blue = min(red, green) + costs[i][2]
            red, green, blue = n_red, n_green, n_blue
        
        return min(red, green, blue)