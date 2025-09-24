class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        k_count = nums.count(k)
        max_gain = 0
        for i in range(1, 51):
            if i == k:
                continue
            curr_count = curr_max = 0
            for num in nums:
                if num == i:
                    curr_count += 1
                elif num == k:
                    curr_count -= 1
                curr_count = max(curr_count, 0)
                curr_max = max(curr_max, curr_count)
            max_gain = max(max_gain, curr_max)
        return k_count + max_gain
                