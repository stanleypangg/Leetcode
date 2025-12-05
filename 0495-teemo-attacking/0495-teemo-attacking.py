class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # teemo attack ashe -> ashe poisoend for duration seconds
        # attack at second t -> Ashe is poisoned during [t, t + duration - 1]
        # if teemo attacks again before timer ends, timer is reset

        # timeSeries: non-decreasing, timeSeries[i] denotes Teemo attacks Ashe at second timeSeries[i]

        res = 0

        for i in range(len(timeSeries) - 1):
            res += min(timeSeries[i + 1] - timeSeries[i], duration)
        
        return res + duration