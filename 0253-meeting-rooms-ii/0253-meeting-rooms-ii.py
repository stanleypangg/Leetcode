class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        res = 0

        for s, e in intervals:
            # while earliest ending room is <= current end
            while heap and heap[0] <= s:
                heapq.heappop(heap)
            heapq.heappush(heap, e)
            res = max(res, len(heap))

        return res