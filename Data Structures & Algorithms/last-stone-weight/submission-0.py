class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x, y = heapq.heappop(stones), heapq.heappop(stones) # two heavist

            if x < y:
                heapq.heappush(stones, x - y)
            
        if stones:
            return abs(stones[0])
        else:
            return 0
