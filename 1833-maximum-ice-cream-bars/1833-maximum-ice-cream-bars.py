class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        min_val = max_val = max(costs)
        counts = [0] * (max_val + 1)

        for cost in costs:
            counts[cost] += 1
            min_val = min(min_val, cost)
        
        res = 0
        for cost, count in enumerate(counts[min_val:], start=min_val):
            if cost == 0:
                res += count
                continue
            if count == 0:
                continue
            
            buy_amt = min(count, coins // cost)
            if buy_amt == 0:
                break
            
            res += buy_amt
            coins -= buy_amt * cost
        
        return res