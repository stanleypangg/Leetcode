class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        max_index = min_index = 0
        i = 0
        j = indexDifference
        while j < n:
            if nums[min_index] > nums[i]:
                min_index = i
            elif nums[max_index] < nums[i]:
                max_index = i

            if abs(nums[min_index] - nums[j]) >= valueDifference:
                return [min_index, j]
            if abs(nums[max_index] - nums[j]) >= valueDifference:
                return [max_index, j]
            i += 1
            j += 1
        return [-1, -1]