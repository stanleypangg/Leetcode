class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 0
        profit = 0

        while j < len(prices) - 1:
            j += 1
            profit = max(profit, prices[j] - prices[i])

            if prices[j] < prices[i]:
                i = j
        
        return profit