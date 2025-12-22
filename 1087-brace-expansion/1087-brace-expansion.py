class Solution:
    def expand(self, s: str) -> List[str]:
        res = []

        options = []
        i = 0
        while i < len(s):
            if s[i] == '{':
                j = s.find('}', i)
                options.append(sorted(s[i + 1 : j].split(',')))
                i = j + 1
            else:
                j = i + 1
                while j < len(s) and s[j] != '{':
                    j += 1
                options.append([s[i : j]])
                i = j

        st = []
        def bt(i):
            if i >= len(options):
                res.append(''.join(st))
                return
            
            for option in options[i]:
                st.append(option)
                bt(i + 1)
                st.pop()
        
        bt(0)
        return res