class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        cur = []
        def bt(i):
            if i >= len(s):
                if len(cur) == 4:
                    res.append('.'.join(cur))
                return
            
            cur.append(s[i])
            bt(i + 1)
            cur.pop()

            if s[i] != '0':
                if i + 1 < len(s):
                    cur.append(s[i: i + 2])
                    bt(i + 2)
                    cur.pop()
                if i + 2 < len(s) and int(s[i: i + 3]) <= 255:
                    cur.append(s[i: i + 3])
                    bt(i + 3)
                    cur.pop()
        
        bt(0)
        return res