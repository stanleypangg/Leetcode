class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()

        count = {}
        for p in power:
            count[p] = count.get(p, 0) + 1
        
        damage = list(count.keys())
        dp = [0] * len(damage)

        maxx = 0
        j = 0
        for i in range(len(dp)):
            while j < i and damage[j] < damage[i] - 2:
                maxx = max(maxx, dp[j])
                j += 1
            
            dp[i] = maxx + damage[i] * count[damage[i]]
        
        return max(dp)