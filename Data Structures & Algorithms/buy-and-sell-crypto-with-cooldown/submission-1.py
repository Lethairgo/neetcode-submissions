class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        next_sell = 0 # the max profit we can get at the next day when we can sell, i.e., dp[i+1][0]
        next_buy = 0 # the max profit we can get at the next day when we can buy, i.e., dp[i+1][1]
        next2_buy = 0 # the max profit we can get at the second next day when we can buy, i.e., dp[i+2][1]

        for i in range(n - 1, -1, -1):
            cur_buy = max(next_sell - prices[i], next_buy)
            cur_sell = max(next2_buy + prices[i], next_sell)

            next2_buy = next_buy
            next_sell = cur_sell
            next_buy = cur_buy

        return next_buy