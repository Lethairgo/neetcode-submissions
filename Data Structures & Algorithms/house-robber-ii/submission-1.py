class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(nums: List[int]) -> int:
            prev1, prev2 = 0, 0

            for num in nums:
                temp = max(prev1 + num, prev2)
                prev1 = prev2
                prev2 = temp
            return prev2
        return max(helper(nums[1:]), helper(nums[: -1]))
        