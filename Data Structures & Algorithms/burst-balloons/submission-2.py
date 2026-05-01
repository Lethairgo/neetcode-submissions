class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        def dfs(arr):
            arr = tuple(arr)
            if not arr:
                return 0
            if arr in dp:
                return dp[arr]
            maximum = 0
            n = len(arr)

            for i in range(n):
                left = arr[i - 1] if i - 1 >= 0 else 1
                right = arr[i + 1] if i + 1 < n else 1
                coins = left * arr[i] * right
                coins += dfs(arr[:i] + arr[i + 1:])
                maximum = max(maximum, coins)
            dp[arr] = maximum
            return maximum


        return dfs(nums)
        