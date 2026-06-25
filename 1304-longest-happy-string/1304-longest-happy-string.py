class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []

        heap = []
        for count, ch in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(heap, (-count, ch))

        while heap:
            count1, ch1 = heapq.heappop(heap)

            if len(res) >= 2 and res[-1] == res[-2] == ch1:
                if not heap:
                    break

                count2, ch2 = heapq.heappop(heap)
                count2 += 1
                res.append(ch2)

                if count2 < 0:
                    heapq.heappush(heap, (count2, ch2))
                
                heapq.heappush(heap, (count1, ch1))
            
            else:
                res.append(ch1)
                count1 += 1

                if count1 < 0:
                    heapq.heappush(heap, (count1, ch1))
        
        return ''.join(res)