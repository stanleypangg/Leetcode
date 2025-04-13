class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0

        for p in prices:
            if p < buy:
                buy = p
            
            profit = max(profit, p - buy)
        
        return profit