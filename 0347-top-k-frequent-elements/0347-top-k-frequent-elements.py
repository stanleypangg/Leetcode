class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        heap = []
        for num in counts:
            if len(heap) < k:
                heapq.heappush(heap, (counts[num], num))
            else:
                heapq.heappushpop(heap, (counts[num], num))
        
        return [pair[1] for pair in heap]