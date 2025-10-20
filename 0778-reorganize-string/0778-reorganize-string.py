class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        heap = [[-f, c] for c, f in freq.items()]
        heapq.heapify(heap) # O(26)

        res = []

        f_one, one = heapq.heappop(heap)
        f_one += 1
        res.append(one)

        while heap:
            f_two, two = heapq.heappop(heap)
            f_two += 1
            res.append(two)

            # char one still has more freq
            if -f_one > 0:
                heapq.heappush(heap, [f_one, one])
            
            f_one, one = f_two, two
        
        if len(res) != len(s):
            return ''
        
        return ''.join(res)
            
