class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        res = total = l = 0
        baskets = defaultdict(int)

        for r, cur in enumerate(fruits):
            total += 1
            baskets[cur] += 1

            while len(baskets) > 2:
                total -= 1
                left = fruits[l]
                baskets[left] -= 1

                if baskets[left] == 0:
                    del baskets[left]
                
                l += 1

            res = max(res, total)                
        
        return res