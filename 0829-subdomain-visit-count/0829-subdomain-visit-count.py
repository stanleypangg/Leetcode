class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            domain_parts = domain.split('.')

            for i in range(len(domain_parts)):
                cur = '.'.join(domain_parts[i:])
                visits[cur] += int(count)
            
        return [f'{count} {domain}' for domain, count in visits.items()]