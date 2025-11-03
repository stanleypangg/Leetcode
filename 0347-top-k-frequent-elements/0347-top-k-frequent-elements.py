class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) space and time
        freq = Counter(nums)
        
        heap = []
        # O(n) iterations
        for num, count in freq.items():
            # O(logn) work per iteration
            if len(heap) == k:
                heapq.heappushpop(heap, (count, num))
            else:
                heapq.heappush(heap, (count, num))
        
        return [num for _, num in heap]