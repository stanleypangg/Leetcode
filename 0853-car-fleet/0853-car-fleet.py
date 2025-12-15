class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort()

        top = 0
        res = 0
        for i in range(len(pairs) - 1, -1, -1):
            p, s = pairs[i]
            time = (target - p) / s

            if time <= top:
                continue
            
            top = time
            res += 1
        
        return res