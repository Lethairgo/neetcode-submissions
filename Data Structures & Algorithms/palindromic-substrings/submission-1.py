class Solution:
    def countSubstrings(self, s: str) -> int:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        center = 0
        right = 0
        result = 0

        for i in range(n):
            left = center * 2 - i
            if i < right:
                p[i] = min(right - i, p[left])
            
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1
                
            if i + p[i] > right:
                right = i + p[i]
                center = i

            result += (p[i] + 1) // 2
        return result