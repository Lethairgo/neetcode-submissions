class Solution:
    def compress(self, chars: List[str]) -> int:
        # two pointers
        left = 0
        index = 0

        for right in range(len(chars)):
            if chars[left] == chars[right]:
                continue
            else:
                length = right - left
                chars[index] = chars[left]
                index += 1
                if length > 1:
                    for char in str(length):
                        chars[index] = char
                        index += 1
                left = right

        length = len(chars) - left
        chars[index] = chars[left]
        index += 1
        if length > 1:
            for char in str(length):
                chars[index] = char
                index += 1
        return index