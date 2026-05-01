class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # prefix sum
        total = sum(nums)
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        if total - nums[0] == 0:
            return 0

        for i in range(1, len(nums)):
            left = prefix[i - 1]
            right = total - nums[i] - prefix[i - 1]
            if left == right:
                return i
            prefix[i] = prefix[i - 1] + nums[i]
        return -1
            