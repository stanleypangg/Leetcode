class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        max_diff = 0
        freq = defaultdict(int)

        for n1, n2 in zip(nums1, nums2):
            d = abs(n1 - n2)
            max_diff = max(d, max_diff)
            freq[d] += 1
        
        k = k1 + k2
        while k > 0 and max_diff > 0:
            amt = min(freq[max_diff], k)
            freq[max_diff] -= amt

            max_diff -= 1
            freq[max_diff] += amt

            k -= amt

        return sum((k ** 2) * v for k, v in freq.items())