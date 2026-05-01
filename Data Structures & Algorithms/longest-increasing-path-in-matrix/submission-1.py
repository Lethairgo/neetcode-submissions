class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dp = {}
        def dfs(r, c, cur):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= cur:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            result = 1
            for dr, dc in directions:
                result = max(result, 1 + dfs(r + dr, c + dc, matrix[r][c]))
            dp[(r, c)] = result
            return result

        max_len = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_len = max(max_len, dfs(r, c, float('-inf')))
        return max_len