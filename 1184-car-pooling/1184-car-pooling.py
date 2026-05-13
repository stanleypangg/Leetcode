class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        max_to = 0

        for num, fromm, to in trips:
            max_to = max(max_to, to)
            diff[fromm] += num
            diff[to] -= num

        if diff[0] > capacity:
            return False
        
        for i in range(1, max_to + 1):
            diff[i] += diff[i - 1]
            if diff[i] > capacity:
                return False
        return True