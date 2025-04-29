class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case for early return
        if not t or not s:
            return ""
        
        t_count, window = {}, {}
        for c in t:
            t_count[c] = t_count.get(c, 0) + 1

        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float('inf')
        l = 0
        for r, c in enumerate(s):
            window[c] = window.get(c, 0) + 1

            if c in t_count and window[c] == t_count[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res, res_len = [l, r], (r - l + 1)
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0] : res[1] + 1] if res else ""
