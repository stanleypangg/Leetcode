from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        
        for c in s:
            hashmap[c] += 1
        for c in t:
            hashmap[c] -= 1

        return all(hashmap[i] == 0 for i in hashmap)