class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        heap = [-c for c in freq.values()]
        heapq.heapify(heap)

        res = presses = 0
        while heap:
            cur = -heapq.heappop(heap)
            res += cur * (presses // 8 + 1)
            presses += 1
        
        return res