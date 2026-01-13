class ATM:
    # denominations: 20, 50, 100, 200, 500

    def __init__(self):
        # assume reversed order for both
        self.denoms = (20, 50, 100, 200, 500)
        self.n = len(self.denoms)
        self.money = [0] * self.n

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, m in enumerate(banknotesCount):
            self.money[i] += m

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * self.n

        for i in range(self.n - 1, -1, -1):
            denom = self.denoms[i]
            notes = min(self.money[i], amount // denom)
            res[i] = notes
            
            amount -= notes * denom
            if amount == 0:
                break
        
        if amount > 0:
            return [-1]

        for i, count in enumerate(res):
            self.money[i] -= count
        return res

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)