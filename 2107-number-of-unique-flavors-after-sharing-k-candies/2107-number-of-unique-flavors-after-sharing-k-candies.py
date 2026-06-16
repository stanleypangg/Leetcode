class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        freq = Counter(candies[k:]) # freq outside the window
        res = len(freq)

        l, r = 0, k - 1
        while r + 1 < len(candies):
            candy_l = candies[l]
            freq[candy_l] = freq.get(candy_l, 0) + 1
            l += 1
            
            r += 1
            candy_r = candies[r]
            freq[candy_r] -= 1
            if freq[candy_r] == 0:
                del freq[candy_r]
            
            res = max(res, len(freq))
        
        return res