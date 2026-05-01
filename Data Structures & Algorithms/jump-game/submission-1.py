class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 1, -1, -1):
            for j in range(nums[i] + 1):
                if i + j >= len(nums) or dp[i + j]:
                    dp[i] = True

        return dp[0]

        