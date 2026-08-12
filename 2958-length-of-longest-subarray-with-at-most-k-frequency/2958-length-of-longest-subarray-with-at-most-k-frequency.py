class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = l = 0
        freq = defaultdict(int)

        for r, r_num in enumerate(nums):
            freq[r_num] += 1
            while freq[r_num] > k and l < r:
                freq[nums[l]] -= 1
                l += 1

            if freq[r_num] <= k:
                res = max(res, r - l + 1)
        
        return res