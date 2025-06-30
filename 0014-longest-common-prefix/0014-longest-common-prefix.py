class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return ''.join(res)
            res.append(strs[0][i])
        
        return ''.join(res)