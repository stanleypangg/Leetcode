class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for cur in asteroids:
            alive = True

            while res and res[-1] > 0 and cur < 0:                
                if abs(res[-1]) < abs(cur):
                    res.pop()
                    continue
                    
                if abs(res[-1]) == abs(cur):
                    res.pop()

                alive = False
                break
                
            if alive:
                res.append(cur)
        
        return res