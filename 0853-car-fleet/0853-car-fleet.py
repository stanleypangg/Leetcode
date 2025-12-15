class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))

        top = res = 0
        for p, s in reversed(pairs):
            time = (target - p) / s

            if time > top:  
                top = time
                res += 1
        
        return res