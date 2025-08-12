class Solution:
    def countSubstrings(self, s: str) -> int:
        # Brute Force
        # Iterate all substrings O(n^2) -> each iteration check palindrome O(n)
        # O(n^3)

        # Expand from center
        # Iterate all characters O(n) -> each iteration check palindrome in left and right
        # Possible to overcount? Don't think so, we have different centers
        # Let's go

        # Probably need to memo something
        # O(n^2) exceeds time limit

        self.res = 0
        memo = defaultdict(dict)

        n = len(s)
        def expand_from_center(l, r): # O(n)
            while l >= 0 and r < n and s[l] == s[r]:
                self.res += 1
                memo[l][r] = True
                l -= 1
                r += 1
        
        for i in range(n): # O(n)
            # O(n)
            expand_from_center(i, i)
            expand_from_center(i, i + 1)
        
        return self.res