class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # we need to find a number to agree on that
        # requires the least amount of changes
        # range each sum can be is 2 to 2 * limit

        n = len(nums)

        # this makes each index correspond to the sum
        # some extra padding for 0 and 1, even tho not possible to make those
        mods = [0] * (2 * limit + 1)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            # 0 mod
            mods[a + b] -= 1
            if a + b + 1 < len(mods):
                mods[a + b + 1] += 1

            # 1 mod
            low = 1 + min(a, b)
            high = limit + max(a, b)
            mods[low] -= 1
            if high + 1 < len(mods):
                mods[high + 1] += 1
        
        res = float('inf')
        mods[1] = n # 2 mod, every pair * 2 = n // 2 * 2 = n
        for i in range(2, len(mods)):
            mods[i] += mods[i - 1]
            res = min(res, mods[i])

        return res