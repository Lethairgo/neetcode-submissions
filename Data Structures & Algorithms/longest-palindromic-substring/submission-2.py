class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        maxLen = 0
        centerInd = 0

        center, right = 0, 0
        for i in range(n):
            left = center * 2 - i
            if i < right:
                p[i] = min(right - i, p[left])
            
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1

            if i + p[i] > right:
                right = i + p[i]
                center = i

            if p[i] > maxLen:
                maxLen = p[i]
                centerInd = i

        start = (centerInd - maxLen) // 2
        return s[start : start + maxLen]
