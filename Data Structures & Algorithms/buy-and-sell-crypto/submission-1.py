class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        i, j = 0, 1

        while i < j and j < len(prices):
            maximum = max(maximum, prices[j] - prices[i])
            if prices[i] > prices[j]:
                i = j
                j += 1
            else:
                j += 1
        return maximum


        