class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # we are in a rotated section
                l = mid + 1
            else:
                # nums[mid] <= nums[r]
                # sorted
                # normal section
                r = mid
        
        return nums[l]