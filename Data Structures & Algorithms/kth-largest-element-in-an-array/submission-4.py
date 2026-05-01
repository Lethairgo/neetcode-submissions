import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            temp = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[temp], nums[i] = nums[i], nums[temp]
                    temp += 1

            nums[temp], nums[right] = nums[right], nums[temp]

            if temp == target:
                return nums[temp]
            elif temp < target:
                left = temp + 1
            else:
                right = temp - 1