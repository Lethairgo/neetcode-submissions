class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n + 1)]  # dp[n+1][amount + 1] = 0, where dp[i][a] means starting from ith coin, how many ways to form a

        # initialization dp, for each coin , we have 1 ways to form 0 by pick nothing
        for i in range(n):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for j in range(1, amount + 1):
                # dont pick i
                dp[i][j] = dp[i + 1][j]

                # pick i
                if coins[i] <= j:
                    dp[i][j] += dp[i][j - coins[i]]
        return dp[0][amount]