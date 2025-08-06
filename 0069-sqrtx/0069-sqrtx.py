class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        l, r = 1, x
        while l <= r:
            mid = (l + r) // 2
            squared = mid ** 2
            if squared == x:
                return mid
            elif squared > x:
                r = mid - 1
            else:
                l = mid + 1
        return r