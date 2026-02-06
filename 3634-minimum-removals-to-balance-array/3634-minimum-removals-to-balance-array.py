class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        nums.sort()

        n = len(nums)
        l, r = 0, 1
        max_length = 0

        while r < n:
            while nums[r] > nums[l] * k:
                l += 1

            max_length = max(max_length, r - l + 1)
            r = max(l + 1, r + 1)

        return n - max_length

# 8, 16, 39, 65, 99