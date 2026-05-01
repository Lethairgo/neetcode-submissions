class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        def dfs(i, target):
            if target == 0:
                return True
            
            if i == len(nums):
                return False
            
            return dfs(i + 1, target - nums[i]) or dfs(i + 1, target)

        return dfs(0, total // 2)
        