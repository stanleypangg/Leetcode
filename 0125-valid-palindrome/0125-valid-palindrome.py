class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = ''.join(c.lower() for c in s if c.isalnum())
        l, r = 0, len(cleaned_s) - 1 

        while l < r:
            if cleaned_s[l] != cleaned_s[r]:
                return False
            l += 1
            r -= 1
        return True