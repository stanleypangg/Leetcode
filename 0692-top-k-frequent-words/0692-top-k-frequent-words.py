class Word:
    def __init__(self, word):
        self.word = word
    
    def __lt__(self, other):
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # O(n)
        freq = Counter(words)
        
        # O(nlogk)
        heap = []
        for w, c in freq.items():
            item = (c, Word(w))

            if len(heap) == k:
                heapq.heappushpop(heap, item)
            else:
                heapq.heappush(heap, item)
        
        # O(klogk)
        heap.sort(key=lambda x: (-x[0], x[1].word))

        # O(k)
        return [w.word for c, w in heap]