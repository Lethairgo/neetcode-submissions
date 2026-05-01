class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        counter = 0
        while nums:
            if counter == n - k:
                return nums[0]
            heapq.heappop(nums)
            counter += 1
