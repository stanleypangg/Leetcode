class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # teemo attack ashe -> ashe poisoend for duration seconds
        # attack at second t -> Ashe is poisoned during [t, t + duration - 1]
        # if teemo attacks again before timer ends, timer is reset

        # timeSeries: non-decreasing, timeSeries[i] denotes Teemo attacks Ashe at second timeSeries[i]

        res = duration

        for i in range(1, len(timeSeries)):
            # check if within prev interval
            prev, curr = timeSeries[i - 1], timeSeries[i]
            if prev <= curr <= prev + duration - 1:
                res += curr - prev
            else:
                res += duration
        
        return res