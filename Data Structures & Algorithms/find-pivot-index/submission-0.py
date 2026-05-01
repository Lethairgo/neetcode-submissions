class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # brute force n^2
        for i, num in enumerate(nums):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1

        