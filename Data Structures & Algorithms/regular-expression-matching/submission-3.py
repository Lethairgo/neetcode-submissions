class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        prev = [False] * (n + 1)
        prev[0] = True

        for j in range(2, n + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 2]

        for i in range(1, m + 1):
            cur = [False] * (n + 1)
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    cur[j] = cur[j - 2]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        cur[j] = cur[j] or prev[j]
                else:
                    if p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                        cur[j] = prev[j - 1]
            prev = cur
        return prev[n]

