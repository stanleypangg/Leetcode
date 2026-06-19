class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)
        email_to_name = {}
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email1 = account[i]
                email_to_name[email1] = name

                for j in range(i + 1, len(account)):
                    email2 = account[j]
                    email_to_name[email2] = name
                    adj[email1].append(email2)
                    adj[email2].append(email1)
        
        visited = set()
        def dfs(cur, account):
            visited.add(cur)
            account.append(cur)
            
            for nei in adj[cur]:
                if nei not in visited:
                    dfs(nei, account)
        
        res = []
        for email in email_to_name:
            if email not in visited:
                name = email_to_name[email]
                account = [name]
                dfs(email, account)
                account[1:] = sorted(account[1:])
                res.append(account)
        
        return res