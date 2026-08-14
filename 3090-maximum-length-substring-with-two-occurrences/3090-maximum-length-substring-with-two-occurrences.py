class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = res = 0
        freq = defaultdict(int)

        for r, c in enumerate(s):
            freq[c] += 1
            while freq[c] > 2:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res