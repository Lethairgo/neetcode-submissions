class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i + 1 < n and nums[i] == nums[i + 1]:
                return nums[i]

        