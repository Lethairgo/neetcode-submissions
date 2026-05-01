class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix sum
        total = sum(nums)
        left = 0

        if total - nums[0] == 0:
            return 0

        for i, num in enumerate(nums):
            right = total - num - left
            if left == right:
                return i
            left += num
        return -1
            