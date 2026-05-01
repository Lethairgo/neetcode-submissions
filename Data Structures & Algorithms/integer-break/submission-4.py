class Solution:
    def integerBreak(self, n: int) -> int:
        # dp
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(
                    dp[i],
                    j * (i - j), # stop cutting
                    j * dp[i - j] # keep cutting the rest
                )

        return dp[n]
        