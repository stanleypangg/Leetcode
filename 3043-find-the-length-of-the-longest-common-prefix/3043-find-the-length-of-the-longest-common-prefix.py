class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        
        trie = {}
        for n in arr1:
            n = str(n)
            curr = trie
            for ch in n:
                if ch not in curr:
                    curr[ch] = {}
                curr = curr[ch]
        
        # find common prefixes in arr2
        for n in arr2:
            n = str(n)
            curr = trie
            length = 0
            for ch in n:
                if ch not in curr:
                    break
                curr = curr[ch]
                length += 1
            res = max(res, length)
        
        return res