class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        # two binary searches
        res_l = None
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    res_l = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        
        if res_l is None:
            return [-1, -1]
        
        res_r = None
        l, r = res_l, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    res_r = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return [res_l, res_r]