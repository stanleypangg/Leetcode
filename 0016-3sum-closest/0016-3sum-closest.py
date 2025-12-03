class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                while j > i + 1 and j < k and nums[j] == nums[j - 1]:
                    j += 1

                total = nums[i] + nums[j] + nums[k]
                if abs(total - target) < abs(res - target):
                    res = total

                if total == target:
                    return total
                elif total < target:
                    j += 1
                else:
                    k -= 1
        
        return res