import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] -= 1
        
        for key in hashmap:
            heapq.heappush(heap, (key, hashmap[key]))
        
        return [h[0] for h in sorted(heap, key=lambda x: x[1])[:k]]