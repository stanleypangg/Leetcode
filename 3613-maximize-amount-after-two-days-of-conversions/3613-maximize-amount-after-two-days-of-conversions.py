class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        # directed graph
        adj = defaultdict(list)
        for (p, q), r in zip(pairs1, rates1):
            adj[(p, 1)].append((q, r))
            adj[(q, 1)].append((p, 1 / r))

        for (p, q), r in zip(pairs2, rates2):
            adj[(p, 2)].append((q, r))
            adj[(q, 2)].append((p, 1 / r))
        
        res = 0
        best = {}
        q = deque([(initialCurrency, 1, 1.0)])

        while q:
            currency, day, amount = q.popleft()
            if best.get((currency, day), 0) >= amount:
                continue
            
            best[(currency, day)] = amount
            for nei, rate in adj[(currency, day)]:
                new_amount = amount * rate
                if day == 1:
                    q.append((nei, 1, new_amount))
                q.append((nei, 2, new_amount))
        
        return best[(initialCurrency, 2)]