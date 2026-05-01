class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        #dp[i][1] = can buy, dp[i][0] = can sell
        dp = [[0] * 2 for _ in range(n + 2)]

        for i in range(n - 1, -1, -1):
            # max profit we can get at day i when we can buy
            dp[i][1] = max(dp[i + 1][0] - prices[i], dp[i + 1][1])
            # max profit we can get at day i when we can sell
            dp[i][0] = max(dp[i + 2][1] + prices[i], dp[i + 1][0])

        return dp[0][1]