class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_Heap = [-count for count in freq.values()]
        heapq.heapify(max_Heap)

        cooldown = deque()
        time = 0

        while max_Heap or cooldown:
            time += 1
            if max_Heap:
                count = heapq.heappop(max_Heap) + 1
                if count != 0:
                    cooldown.append((time + n, count))
            
            if cooldown and cooldown[0][0] == time:
                _, count = cooldown.popleft()
                heapq.heappush(max_Heap, count)
        return time
        