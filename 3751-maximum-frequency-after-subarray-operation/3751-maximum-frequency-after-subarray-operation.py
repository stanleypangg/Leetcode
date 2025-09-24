class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        k_count = nums.count(k)
        max_count = 0
        for i in range(1, 51):
            if i == k:
                continue
            curr_count = 0
            curr_max = 0
            for num in nums:
                if num == i:
                    curr_count += 1
                if num == k:
                    curr_count -= 1
                if curr_count < 0:
                    curr_count = 0
                curr_max = max(curr_max, curr_count)
            max_count = max(max_count, curr_max)
        return k_count + max_count
                