class Solution:
    def reorganizeString(self, s: str) -> str:
        # get count
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        # alternate between most common letters
        # use a max heap
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)

        res = []
        prev_freq, prev_char = 0, ''
        while heap:
            freq, char = heapq.heappop(heap)
            res.append(char)

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))
            
            freq += 1
            prev_freq, prev_char = freq, char
        
        if len(res) != len(s):
            return ''

        return ''.join(res)