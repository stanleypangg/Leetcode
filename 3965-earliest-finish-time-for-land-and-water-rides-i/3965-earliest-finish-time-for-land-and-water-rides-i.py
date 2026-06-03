class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = float('inf')

        for land_start, land_duration in zip(landStartTime, landDuration):
            land_end = land_start + land_duration

            for water_start, water_duration in zip(waterStartTime, waterDuration):
                water_end = water_start + water_duration

                finish1 = max(land_end, water_start) + water_duration
                finish2 = max(water_end, land_start) + land_duration

                res = min(res, finish1, finish2)
        
        return res