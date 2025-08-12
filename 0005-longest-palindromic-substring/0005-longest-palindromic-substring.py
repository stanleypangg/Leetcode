class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Naive O(n^3)
        # Iterate every substring -> O(n^2), check is paldindrome on every substring -> O(n)
        # Thus, total time is O(n^3)

        # Optimal O(n^2)
        # Iterate on every char -> O(n), check if left and right substring is palindrome -> O(n)
        # Thus, total time is O(n^2)
        # This small change shaves off a bunch of time

        res_l = res_r = 0
        n = len(s)

        # Iterate every char
        for i in range(n):
            # Expand from center

            # Odd case "one center"
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                # Update if longer palindrome found
                if res_r - res_l < r - l:
                    res_r, res_l = r, l
                l -= 1
                r += 1
            
            # Even case "two centers"
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                # Update if longer palindrome found
                if res_r - res_l < r - l:
                    res_r, res_l = r, l
                l -= 1
                r += 1
            
        return s[res_l : res_r + 1]