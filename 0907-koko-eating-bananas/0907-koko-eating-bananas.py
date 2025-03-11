class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while l <= r:
            mid = (l + r) // 2
            # Use ceil
            time = sum(math.ceil(i / mid) for i in piles)

            if time <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return k