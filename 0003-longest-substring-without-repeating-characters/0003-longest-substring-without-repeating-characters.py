class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = 1

        # O(26) = O(1) space
        seen = set()
        seen.add(s[0])

        l, r = 0, 1
        while r < len(s):
            # Want to see if s[r] cold be added to the substring
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r - l + 1)
            else:
                # if s[r] seen, we want to keep moving l until no more duplicate
                while s[l] != s[r] and l < r:
                    seen.remove(s[l])
                    l += 1
                # s[l] is s[r] now
                l += 1
            r += 1
            
        return res