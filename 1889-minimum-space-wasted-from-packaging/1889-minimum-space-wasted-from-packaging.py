class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        MOD = 1000000007
        n, m = len(packages), len(boxes)
        packages.sort()

        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + packages[i - 1]
        
        res = float('inf')
        for box in boxes:
            waste = prev = 0
            box.sort()

            for size in box:
                # finds first package that cannot fit in size
                idx = bisect.bisect_right(packages, size)
                num_boxes = idx - prev
                package_sum = prefix[idx] - prefix[prev]
                waste += num_boxes * size - package_sum
                prev = idx
            
            if prev == len(packages):
                # all packages have been processed
                res = min(res, waste)
        
        return -1 if res == float('inf') else res % MOD