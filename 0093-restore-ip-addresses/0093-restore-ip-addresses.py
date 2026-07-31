class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def bt(i, path):
            if len(path) == 4:
                if i == len(s):
                    res.append('.'.join(path))
                return
            
            for j in range(1, 4):
                if i + j > len(s):
                    break

                part = s[i: i + j]

                if (part[0] == '0' and j > 1) or int(part) > 255:
                    continue
                
                bt(i + j, path + [part])
        
        bt(0, [])
        return res