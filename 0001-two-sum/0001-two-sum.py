class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force O(n^2) time, O(1) space
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        indices = {}
        for i in range(len(nums)):
            if target - nums[i] in indices:
                return [i, indices[target - nums[i]]]
            
            indices[nums[i]] = i