class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = set()
        subset = []
        nums.sort()
        def dfs(i):
            if i == len(nums):
                result.add(tuple(subset))
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return [list(x) for x in result]