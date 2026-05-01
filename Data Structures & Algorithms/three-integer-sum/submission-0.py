class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1

            while j < k:
                target = val + nums[j] + nums[k]
                if target > 0:
                    k -= 1
                elif target < 0:
                    j += 1
                elif target == 0:
                    result.append([val, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return result


        