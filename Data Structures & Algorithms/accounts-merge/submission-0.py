class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Iterative DFS

        graph = defaultdict(list)
        email_to_name = {}

        # build graph, using emails as nodes
        for account in accounts:
            name = account[0]

            first = account[1]
            email_to_name[first] = name

            emails = account[2:]

            for email in emails:
                email_to_name[email] = name
                graph[first].append(email)
                graph[email].append(first)

        visited = set()
        stack = []
        result = []

        for email in email_to_name:
            if email in visited:
                continue
            
            stack.append(email)
            visited.add(email)
            component = []
            while stack:
                cur = stack.pop()
                component.append(cur)

                for nei in graph[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)

            result.append([email_to_name[email]] + sorted(component))
        return result



        