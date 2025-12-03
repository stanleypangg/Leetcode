class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap: group key -> anagrams
        groups = {}

        for string in strs:
            # form a key
            # use a counter

            # array b/c fixed number of characters + convertible to tuple
            # tuple is immutable -> can be used for the key
            # all anagrams will have the same counter
            counter = [0] * 26 
            for c in string:
                # subtract ord('a') to offset to 0, 1, 2, 3...
                counter[ord(c) - ord('a')] += 1
            
            key = tuple(counter)
            if key not in groups:
                groups[key] = []
            groups[key].append(string)
        
        return [group for group in groups.values()]