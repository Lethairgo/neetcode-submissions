class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        neighbors = defaultdict(list)

        for u, v, t in times:
            neighbors[u].append((v, t))

        minHeap = [(0, k)]
        visited = {}

        while minHeap:
            time, node = heapq.heappop(minHeap)
                        
            if node in visited:
                continue
            visited[node] = time

            for neighbor, t in neighbors[node]:
                if neighbor not in visited:
                    heapq.heappush(minHeap,(time + t, neighbor))
        return max(visited.values()) if len(visited) == n else -1


        