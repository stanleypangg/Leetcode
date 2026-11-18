class Solution:
    def minMoves(self, nums: list[int]) -> int:
        freq = {}
        minimum = float('inf')

        for n in nums:
            minimum = min(n, minimum)
            freq[n] = freq.get(n, 0) + 1
        
        total = 0
        for n in freq:
            if n == minimum:
                continue
            total += (n - minimum) * freq[n]
        
        return total