class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        hashmap = defaultdict(list)

        for tx in transactions:
            name, time, _, city = tx.split(',')
            hashmap[name].append((int(time), city))

        for tx in transactions:
            name, time, amount, city = tx.split(',')
            time = int(time)

            if int(amount) > 1000:
                res.append(tx)
                continue
            
            for other_time, other_city in hashmap[name]:
                if city != other_city and abs(time - other_time) <= 60:
                    res.append(tx)
                    break

        return res