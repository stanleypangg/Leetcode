class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        count = 0

        for x, y in points:
            dist = -(x**2 + y**2)
            if count < k:
                heapq.heappush(heap, (dist, x, y))
                count += 1
            else:
                heapq.heappushpop(heap, (dist, x, y))
        
        return [[x, y] for (dist, x, y) in heap]