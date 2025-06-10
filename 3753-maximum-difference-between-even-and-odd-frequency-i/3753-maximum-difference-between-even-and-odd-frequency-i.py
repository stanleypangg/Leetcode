class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        max_odd = float('-inf')
        min_even = float('inf')

        for c in freq:
            count = freq[c]
            if count % 2 == 0:
                min_even = min(min_even, count)
            else:
                max_odd = max(max_odd, count)
        
        return max_odd - min_even