class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))] #dp[i][0] = max, dp[i][1] = min,
        result = nums[0]
        dp[0][0], dp[0][1] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = max(nums[i], dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i])
            dp[i][1] = min(nums[i], dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i])
            result = max(result, dp[i][0])

        return result
        