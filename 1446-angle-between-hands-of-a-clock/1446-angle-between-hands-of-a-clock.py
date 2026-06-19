class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # each tick is 6deg
        # each hour has 5 ticks for total of 30 deg

        hour_pos = hour * 30 + (minutes / 2)
        min_pos = minutes * 6

        dist = abs(hour_pos - min_pos)
        return min(dist, abs(360 - dist))