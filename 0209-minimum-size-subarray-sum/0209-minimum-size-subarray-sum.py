class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = math.inf
        total = 0
        
        i = j = 0
        for j in range(len(nums)):
            total += nums[j]

            while total >= target:
                res = min(j - i + 1, res)

                if total - nums[i] >= target:
                    total -= nums[i]
                    i += 1
                else:
                    break
        
        return 0 if res == math.inf else res