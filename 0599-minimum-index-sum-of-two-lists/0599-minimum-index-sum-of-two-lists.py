class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n = len(list1)
        m = len(list2)

        small = list1 if n <= m else list2
        big = list2 if n <= m else list1

        hashmap = {}
        for i, string in enumerate(small):
            if string not in hashmap:
                hashmap[string] = i
        
        res = []
        least = float('inf')
        for i, string in enumerate(big):
            if string in hashmap:
                index_sum = i + hashmap[string]
                if index_sum <= least:
                    if index_sum < least:
                        least = index_sum
                        res = []
                    res.append(string)
        
        return res