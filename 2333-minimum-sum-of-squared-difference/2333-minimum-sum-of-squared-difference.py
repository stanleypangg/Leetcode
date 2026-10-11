class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        diff = [-abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        diff.sort()

        k = k1 + k2
        while k:
            if diff[0] == 0:
                break   
            
            idx = bisect.bisect(diff, diff[0], lo=0, hi=min(n, k))
            if idx >= n or k <= idx:
                mod = 1
            else:
                mod = min(diff[idx] - diff[0], k // idx)

            diff[:idx] = [diff[0] + mod] * idx
            k -= idx * mod

        return sum(d ** 2 for d in diff)