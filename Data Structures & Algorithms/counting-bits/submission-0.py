class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (1 & i)

        return dp
        