class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # [4,3,2,1]
        # [1,1,1,0]

        # [1,0,1]
        # [-1,-1,-1]

        n = len(nums)
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] -= 1
            diff[r + 1] += 1
        
        prefix = 0
        for i in range(n):
            prefix += diff[i]
            if nums[i] + prefix > 0:
                return False
        
        return True