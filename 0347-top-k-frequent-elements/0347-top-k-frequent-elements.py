class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # better than O(nlogn) means no sorting
        counter = {} # O(k) space
        for num in nums: # O(n) time
            counter[num] = counter.get(num, 0) + 1
        
        heap = [] # O(k) space
        for num, freq in counter.items(): # O(k) iterations
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))
        
        return [num for _, num in heap]
