class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search
        max_weight = max(weights)
        total = sum(weights)

        left, right = max_weight, total

        while left < right:
            capacity = (left + right) // 2

            day_used = 1
            cur = 0

            for weight in weights:
                if cur + weight <= capacity:
                    cur += weight
                else:
                    day_used += 1
                    cur = weight

            if day_used > days:
                left = capacity + 1
            else:
                right = capacity

        return right