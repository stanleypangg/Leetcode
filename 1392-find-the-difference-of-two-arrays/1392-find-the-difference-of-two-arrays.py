class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[], []]

        for n in set(nums1):
            if n not in nums2:
                res[0].append(n)
        
        for n in set(nums2):
            if n not in nums1:
                res[1].append(n)
        
        return res