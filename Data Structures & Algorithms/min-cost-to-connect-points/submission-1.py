class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minDist = [float('inf')] * n
        visited = [False] * n
        result = 0

        minDist[0] = 0

        for _ in range(n):
            cur = -1
            for i in range(n):
                if not visited[i] and (cur == -1 or minDist[i] < minDist[cur]):
                    cur = i

            visited[cur] = True
            result += minDist[cur]

            x1, y1 = points[cur]
            for j in range(n):
                if not visited[j]:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    minDist[j] = min(dist, minDist[j])

        return result
        