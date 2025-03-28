class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Array and hashing
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        count = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        return count[:k]
