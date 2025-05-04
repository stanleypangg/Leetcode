class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for item in details:
            age = int(item[11:13])
            if age > 60:
                res += 1
        return res