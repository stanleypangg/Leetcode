class SparseVector:
    def __init__(self, nums: List[int]):
        self.map = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.map[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0

        if len(self.map) < len(vec.map):
            smaller, bigger = self.map, vec.map
        else:
            smaller, bigger = vec.map, self.map
        
        for index in smaller:
            if index in bigger:
                res += bigger[index] * smaller[index]
        
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)