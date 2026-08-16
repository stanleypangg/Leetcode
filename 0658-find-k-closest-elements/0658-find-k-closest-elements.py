class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # nlogk
        heap = []

        for n in arr:
            closeness = abs(n - x) 
            if len(heap) < k:
                heapq.heappush(heap, (-closeness, -n))
            else:
                heapq.heappushpop(heap, (-closeness, -n))
        
        return list(sorted(-n for _, n in heap))