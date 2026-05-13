class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        arr = [0] * length
        
        for startIdx, endIdx, inc in updates:
            arr[startIdx] += inc
            if endIdx + 1 < length:
                arr[endIdx + 1] -= inc
        
        for i in range(1, length):
            arr[i] += arr[i - 1]
        return arr