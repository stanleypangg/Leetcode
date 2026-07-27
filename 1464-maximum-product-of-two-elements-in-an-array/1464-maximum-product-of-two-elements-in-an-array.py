class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []
        for n in nums:
            if len(heap) < 2:
                heapq.heappush(heap, n)
            else:
                heapq.heappushpop(heap, n)
        
        return (heap[0] - 1) * (heap[1] - 1)