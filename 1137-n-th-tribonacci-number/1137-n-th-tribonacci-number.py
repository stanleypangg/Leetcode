class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        one, two, three = 0, 1, 1
        for _ in range(3, n + 1):
            cur = one + two + three
            one, two, three = two, three, cur
        
        return cur