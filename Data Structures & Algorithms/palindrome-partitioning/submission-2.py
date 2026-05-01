class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        result = []
        path = []

        def backtracking(start):
            if start == len(s):
                result.append(path.copy())
                return

            for end in range(start, len(s)):
                if dp[start][end]:
                    path.append(s[start: end + 1])
                    backtracking(end + 1)
                    path.pop()
        backtracking(0)
        return result