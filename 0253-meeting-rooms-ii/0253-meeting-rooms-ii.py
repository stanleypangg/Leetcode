class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        heap = []

        # since intervals is sorted, everything in heap has guarateed start <= cur_start
        # min heap by end time

        for start, end in intervals:
            # while they don't overlap
            # min heap grabs current largest end
            while heap and heap[0] <= start:
                heapq.heappop(heap)

            # by here, if heap is non-empty, we have # of overlapping rooms
            heapq.heappush(heap, end)
            res = max(res, len(heap))

        return res