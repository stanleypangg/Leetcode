class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            n = nums[mid]

            if n == target:
                return mid
            elif n < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1