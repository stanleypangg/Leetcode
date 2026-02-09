class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        i = j = None
        count = 0

        for k in range(len(s1)):
            if s1[k] != s2[k]:
                count += 1
                if i is None: i = k
                elif j is None: j = k
            
            if count > 2:
                return False

        if count == 0:
            return True
        elif count == 1:
            return False
        
        return s1[i] == s2[j] and s1[j] == s2[i]