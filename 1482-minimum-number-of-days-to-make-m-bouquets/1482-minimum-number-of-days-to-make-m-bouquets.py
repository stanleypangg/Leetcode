class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def solve(mid):
            num_bouquets = count = 0
            for day in bloomDay:
                if day <= mid:
                    count += 1
                else:
                    count = 0

                if count == k:
                    num_bouquets += 1
                    count = 0
                
                if num_bouquets == m:
                    return True
            
            return False

        if len(bloomDay) < m * k:
            return -1
        
        l = min(bloomDay)
        r = max(bloomDay)
        res = -1

        while l <= r:
            mid = (l + r) // 2

            if solve(mid):
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        
        return res