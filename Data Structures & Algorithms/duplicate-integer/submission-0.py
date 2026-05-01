class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set(nums)
        return len(result) != len(nums)
        