class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            tempMax = max(nums[i], curMax * nums[i], curMin * nums[i])
            tempMin = min(nums[i], curMax * nums[i], curMin * nums[i])
            curMax, curMin = tempMax, tempMin
            result = max(result, curMax)

        return result