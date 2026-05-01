class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        left, right = 1, piles[-1]
        result = float('inf')

        while left <= right:
            mid = (left + right) // 2
            temp = 0
            for pile in piles:
                temp += math.ceil(pile / mid)
            if temp <= h:
                result = min(mid, result)
                right = mid - 1
            else:
                left = mid + 1

        return result
        