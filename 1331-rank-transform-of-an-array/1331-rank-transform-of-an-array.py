class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = [1] * (len(arr))
        sort = sorted(enumerate(arr), key=lambda x: x[1])

        counter = 1
        for i in range(1, len(sort)):
            j, cur = sort[i]
            _, prev = sort[i - 1]

            if cur != prev:
                counter += 1
            res[j] = counter
        
        return res