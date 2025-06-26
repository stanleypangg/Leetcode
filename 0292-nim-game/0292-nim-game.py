class Solution:
    def canWinNim(self, n: int) -> bool:
        # base case
        # n = 1, 2, 3: true
        # n = 4: false
        # n = 5: remove 1 -> not f(4) = True
        # n = 6: remove 2 -> true
        # n = 7: remove 3 -> true
        # n = 8 = 

        # true = 1, 2, 3, 5, 6, 7, 9, 10, 11
        # false = 4, 8, 12

        return n % 4 != 0