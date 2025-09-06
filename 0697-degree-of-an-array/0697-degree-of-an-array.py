class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        indices = {} # num -> (l, r)
        count = {} # num -> count
        for i, n in enumerate(nums):
            count[n] = count.get(n, 0) + 1
            if n not in indices:
                indices[n] = [i, i]
            indices[n][1] = i

        max_deg = [n for n in count if count[n] == max(count.values())]

        return min(indices[n][1] - indices[n][0] + 1 for n in max_deg)