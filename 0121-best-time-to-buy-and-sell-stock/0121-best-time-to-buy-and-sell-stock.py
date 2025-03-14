class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        profit = 0

        while j < len(prices):
            profit = max(profit, prices[j] - prices[i])
            if prices[j] < prices[i]:
                i = j
            else:
                j += 1
        
        return profit