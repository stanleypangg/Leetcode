class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
        
        # define fixed window
        window = {}
        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1
        
        l, r = 0, len(s1)
        # sliding window
        while r <= len(s2):
            if window == s1_count:
                return True

            if r == len(s2):
                break

            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            
            window[s2[r]] = window.get(s2[r], 0) + 1
            
            l += 1
            r += 1

        return False