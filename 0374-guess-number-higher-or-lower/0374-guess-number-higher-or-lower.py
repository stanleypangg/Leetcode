# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2
            ret = guess(mid)

            if ret == 0:
                return mid
            elif ret == -1:
                r = mid - 1
            else:
                l = mid + 1
        
        
