class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []

        for price, amount, order_type in orders:
            if order_type == 0:
                while sell and sell[0][0] <= price:
                    sell_price, sell_amount = sell[0]
                    if amount >= sell_amount:
                        amount -= sell_amount
                        heapq.heappop(sell)
                    else:
                        sell[0][1] -= amount
                        amount = 0
                        break
            else:
                while buy and buy[0][0] >= price:
                    buy_price, buy_amount = buy[0]
                    if amount >= buy_amount:
                        amount -= buy_amount
                        heapq.heappop_max(buy)
                    else:
                        buy[0][1] -= amount
                        amount = 0
                        break
            
            if amount > 0:
                if order_type == 0:
                    heapq.heappush_max(buy, [price, amount])
                else:
                    heapq.heappush(sell, [price, amount])
        
        res = sum(amt for _, amt in buy) + sum(amt for _, amt in sell)
        return res % 1000000007