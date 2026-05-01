class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m < n:
            text1, text2 = text2, text1
            m, n = n, m

        prev = [0] * (n + 1)
        cur = [0] * (n + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    cur[j] = 1 + prev[j + 1]
                else:
                    cur[j] = max(cur[j + 1], prev[j])
            prev, cur = cur, prev

        return prev[0]