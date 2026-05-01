class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = max(weights)
        total = sum(weights)

        for capacity in range(max_weight, total + 1):
            day_used = 1
            cur = 0

            for weight in weights:
                if cur + weight <= capacity:
                    cur += weight
                else:
                    day_used += 1
                    cur = weight
                    if day_used > days:
                        break
            if day_used <= days:
                return capacity