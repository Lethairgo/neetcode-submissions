class Solution:
    def reverseBits(self, n: int) -> int:
        stack = []

        for i in range(31, -1, -1):
            stack.append((n >> i) & 1)
        
        result = 0
        while stack:
            result = (result << 1) | stack.pop()

        return result
