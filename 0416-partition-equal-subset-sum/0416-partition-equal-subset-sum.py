class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2

        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            next_dp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                next_dp.add(t + nums[i])
                next_dp.add(t)
            dp = next_dp

        return True if target in dp else False