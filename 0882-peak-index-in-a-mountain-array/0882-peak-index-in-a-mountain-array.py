class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # mountain array
        # increasing sub arr, then decreasing sub arr
        # target has arr[mid-1] > arr[mid] > arr[mid+1]
        # target cannot be 0 or n - 1
        # can we binary search this?

        l, r = 0, len(arr) - 1

        while l < r:
            mid = (l + r) // 2

            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid
        
        return l