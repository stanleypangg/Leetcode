class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        s_map = {}
        for c in s:
            s_map[c] = s_map.get(c, 0) + 1
        
        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        return s_map == t_map