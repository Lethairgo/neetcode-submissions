class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)

        cur = 0
        result = 0
        count[0] = 1

        for num in nums:
            cur += num
            result += count[cur - k]
            count[cur] += 1
        return result

