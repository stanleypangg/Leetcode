class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # customers[i] = 'Y' -> customers come in at hour i
        # customers[i] = 'N' -> no customers come at the ith hour
        # shop closes at 0 <= j <= n
        # penalty -> for every hour shop is open and no customers come, increase by 1
        #         -> for every hr shop is closed and no customers come, penalty increase by 1
        # return earliest hr at which shiop must be closed to incur a min penalty

        # penalty = sum(customers[i] == 'N' for 0 <= i < j) + sum(customers[i] == 'Y' for j <= i < n)

        res = 0
        min_penalty = penalty = customers.count('Y')

        for i in range(1, len(customers) + 1):
            if customers[i - 1] == 'Y':
                penalty -= 1
            else:
                penalty += 1
            
            if penalty < min_penalty:
                penalty = min_penalty
                res = i
        
        return res