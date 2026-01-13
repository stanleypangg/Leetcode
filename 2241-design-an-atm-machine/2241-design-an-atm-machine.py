class ATM:
    # denominations: 20, 50, 100, 200, 500
    DENOMS = (20, 50, 100, 200, 500)

    def __init__(self):
        self.money = [0] * len(self.DENOMS)

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, count in enumerate(banknotesCount):
            self.money[i] += count

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * len(self.DENOMS)
        remaining = amount

        for i in range(len(self.DENOMS) - 1, -1, -1):
            denom = self.DENOMS[i]
            take = min(self.money[i], remaining // denom)
            res[i] = take
            remaining -= take * denom

            if remaining == 0:
                break
        
        if remaining != 0:
            return [-1]

        for i in range(len(self.DENOMS)):
            self.money[i] -= res[i]
            
        return res

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)