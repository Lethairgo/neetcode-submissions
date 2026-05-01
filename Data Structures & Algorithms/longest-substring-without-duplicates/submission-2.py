class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLen = 0
        chars = set()
        i, j = 0, 0

        while j < len(s):
            if s[j] not in chars:
                chars.add(s[j])
                j += 1
                maxLen = max(maxLen, j - i)
            else:
                chars.remove(s[i])
                i += 1
        return maxLen
            