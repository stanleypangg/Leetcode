class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            counter = [0] * 26
            for c in string:
                counter[ord(c) - ord('a')] += 1
            
            key = tuple(counter)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(string)
        
        return list(hashmap.values())