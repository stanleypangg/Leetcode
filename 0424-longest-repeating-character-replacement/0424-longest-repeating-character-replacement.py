class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        window = {}

        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            # check if replacement is needed
            if len(window) < 1:
                continue
            
            total = sum(window.values())
            while l < r and total - max(window.values()) > k:
                window[s[l]] -= 1
                total -= 1
                max_count = max(window.values())
                l += 1

            res = max(res, r - l + 1)

        return res