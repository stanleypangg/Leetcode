class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        res = float('inf')

        while i < len(nums1) and j < len(nums2):
            a = nums1[i]
            b = nums2[j]

            if a == b:
                res = min(res, a)
                i += 1
                j += 1
            elif a < b:
                i += 1
            else:
                j += 1
        
        return res if res != float('inf') else -1