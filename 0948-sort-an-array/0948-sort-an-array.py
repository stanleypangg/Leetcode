class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)
        
    def merge(self, lst1, lst2):
        res = []
        i = j = 0
        while i < len(lst1) and j < len(lst2):
            if lst1[i] < lst2[j]:
                res.append(lst1[i])
                i += 1
            else:
                res.append(lst2[j])
                j += 1

        res.extend(lst1[i:])
        res.extend(lst2[j:])

        return res