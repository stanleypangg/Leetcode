class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = max_length = 0

        for r, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            most_common_count = max(count.values())
            if sum(count.values()) - most_common_count > k:
                count[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        
        return max_length