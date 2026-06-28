class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 1

        for x in freq:
            if x == 1:
                count = freq[1]
                if count % 2 == 0:
                    count -= 1
                res = max(res, count)
                continue
            
            cur = x
            size = 0

            while cur in freq and freq[cur] >= 2:
                size += 2
                cur *= cur
            
            if cur in freq:
                size += 1
            else:
                size -= 1
            
            res = max(res, size)
        
        return res