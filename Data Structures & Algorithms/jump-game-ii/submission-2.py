class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque()
        visited = set()

        q.append((0, 0)) # index, steps

        while q:
            i, steps = q.popleft()
            if i == n - 1:
                return steps

            for j in range(i + 1, min(n, i + nums[i] + 1)):
                if j not in visited:
                    q.append((j, steps + 1))
                    visited.add(j)
    