class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        result = 0

        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            
            for nei in adj[node]:
                dfs(nei)

        for i in range(n):
            if i not in visited:
                result += 1
                dfs(i)
        return result
        