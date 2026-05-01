class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union Find
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)


        # initializing and union
        for account in accounts:
            name = account[0]
            first = account[1]

            if first not in parent:
                parent[first] = first
            email_to_name[first] = name

            for email in account[2:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                
                union(first, email)

        
        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)

        result = []
        for root in groups:
            result.append([email_to_name[root]] + sorted(groups[root]))

        return result
