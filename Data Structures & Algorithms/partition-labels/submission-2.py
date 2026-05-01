class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, char in enumerate(s):
            last[char] = i

        result = []
        start = end = 0
        for i in range(len(s)):
            end = max(end, last[s[i]])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result
