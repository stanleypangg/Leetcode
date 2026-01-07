class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1 

        for n in arr1:
            while n > 0 and n not in prefixes:
                prefixes.add(n)
                n //= 10
        
        res = 0
        for n in arr2:
            while n > 0:
                if n in prefixes:
                    res = max(res, len(str(n)))
                n //= 10
        
        return res