class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = -1
        n = len(heights)
        for i in range(n):
            left, right = i - 1, i + 1
            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            while right < n and heights[right] >= heights[i]:
                right += 1

            area = heights[i] * (right - left - 1)
            result = max(area, result)
        return result