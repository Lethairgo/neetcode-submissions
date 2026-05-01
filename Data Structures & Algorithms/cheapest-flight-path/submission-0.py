class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, price in flights:
            adj[u].append((v, price))
        
        minHeap = [(0, src, 0)] # (total cost, current city, stop used)
        dist = {} # dist[node][edges] = minimum cost when using edges to reach node

        while minHeap:
            cost, node, edges = heapq.heappop(minHeap)
            if node == dst:
                return cost

            if edges == k + 1:
                continue
            
            if (node, edges) in dist and dist[(node, edges)] < cost:
                continue

            for neighbor, price in adj[node]:
                newCost = cost + price
                newEdges = edges + 1

                if (neighbor, newEdges) not in dist or newCost < dist[(neighbor, newEdges)]:
                    dist[(neighbor, newEdges)] = newCost
                    heapq.heappush(minHeap, (newCost, neighbor, newEdges))
        return -1

        