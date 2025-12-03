class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                # unlike 3sum, duplicates dont matter here
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