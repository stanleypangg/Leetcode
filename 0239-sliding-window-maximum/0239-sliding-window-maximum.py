class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        q = deque()
        for r in range(len(nums)):
            l = r - k + 1
            while q and q[0][1] < l:
                q.popleft()

            while q and nums[r] >= q[-1][0]:
                q.pop()
                
            q.append((nums[r], r))

            if l >= 0:
                res.append(q[0][0])
        
        return res