class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        email_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    union(i, email_to_account[email])
                else:
                    email_to_account[email] = i
        
        groups = defaultdict(list)
        for email, i in email_to_account.items():
            root = find(i)
            groups[root].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in groups.items()]