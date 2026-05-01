class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        farthest = 0
        end = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == end:
                end = farthest
                steps += 1
        return steps
