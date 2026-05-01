class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {ch: i for i, ch in enumerate(s)}
        result = []
        i = 0

        while i < len(s):
            right = last[s[i]]
            j = i
            while j < right:
                right = max(right, last[s[j]])
                j += 1
            result.append(right - i + 1)
            i = right + 1

        return result