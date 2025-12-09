class Bank:
    # transaction is valid if -> given account number(s) are between 1 and n
    # amount of money withdrawn or transfered is less than or equal to the balance of the account

    def __init__(self, balance: List[int]):
        # balance[i] = (i + 1)th initial balance
        self.balance = balance
    
    def _validate_transaction(self, account: int, money: int) -> bool:
        # validate that account has enough funds
        # shift one -1 for 0-indexing
        return self.balance[account - 1] >= money
    
    def _validate_acct(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (self._validate_acct(account1) and self._validate_acct(account2)):
            return False
        if not self._validate_transaction(account1, money):
            return False
        
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money

        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._validate_acct(account):
            return False

        self.balance[account - 1] += money

        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._validate_acct(account):
            return False
        if not self._validate_transaction(account, money):
            return False
        
        self.balance[account - 1] -= money

        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)