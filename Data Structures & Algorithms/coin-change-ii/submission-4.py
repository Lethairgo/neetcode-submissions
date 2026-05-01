class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [0] * (amount + 1) # dp[amount + 1] = 0, where dp[a] means how many ways to form a

        # initialization dp, we have 1 ways to form 0 by pick nothing
        dp[0] = 1

        for coin in coins:
            for a in range(coin, amount + 1):
                # current # of ways to form a plus # of ways to form amount - coin
                dp[a] += dp[a - coin]

        return dp[amount]