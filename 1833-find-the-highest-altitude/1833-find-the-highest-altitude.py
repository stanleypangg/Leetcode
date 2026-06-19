class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = altitude = 0
        for g in gain:
            altitude += g
            res = max(res, altitude)
        return res