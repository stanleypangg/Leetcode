class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # for each 0 <= i < num1.length find j s.t. nums1[i] == nums[j]
        # and detrermine the next greater element in nums2[j], if none, the ans is -1

        # O(n) time and space, n = nums1.length
        ans = [-1] * len(nums1)

        # O(n) time and space
        hashmap = {}
        for i, n in enumerate(nums1):
            hashmap[n] = i
        
        # O(m) time and space, m = nums2.length
        st = []
        for i, n in enumerate(nums2):
            while st and n > st[-1]:
                top = st.pop()
                if top in hashmap:
                    index = hashmap[top]
                    ans[index] = n
            
            st.append(n)
        
        return ans