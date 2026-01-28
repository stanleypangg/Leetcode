# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # celebrity knows no one, but everyone knows the celebrity
        l, r = 0, 1
        while r < n:
            if knows(l, r):
                l = r
            r += 1
        
        for i in range(n):
            if i == l:
                continue
            if not knows(i, l) or knows(l, i):
                return -1

        return l