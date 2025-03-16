class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = defaultdict(int)
        for c in ransomNote:
            hashmap[c] += 1
        
        for c in magazine:
            hashmap[c] -= 1
        
        return all(count <= 0 for count in hashmap.values())