class Solution:
    def minEnd(self, n: int, x: int) -> int:
        k = n - 1
        res = x
        bit = 0

        while k:
            if ((res >> bit) & 1) == 0:
                if k & 1:
                    res |= 1 << bit
                k >>= 1
            bit += 1

        return res