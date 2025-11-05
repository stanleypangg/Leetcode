class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # n = len(piles)
        # h hours
        # k bananas per hour
        
        # each hr: choose some pile and eat k bananas from that pile
        # if less than k bananas, eats all instead and idles

        # return minimum integer k s.t. she can eat all bananads within h hours

        # binary search to find minimum integer k
        
        l = 1
        r = k = max(piles)

        # (n log n)
        while l <= r:
            mid = (l + r) // 2

            time = h
            for pile in piles:
                time -= math.ceil(pile / mid)
                if time < 0:
                    break
            
            if time >= 0:
                k = mid
                r = mid - 1
            else:
                l = mid + 1

        return k