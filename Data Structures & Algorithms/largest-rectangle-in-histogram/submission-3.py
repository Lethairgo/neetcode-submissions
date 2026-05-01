class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0
        n = len(heights)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                right = i
                width = right - left - 1
                area = height * width
                result = max(result, area)
            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            right = n
            width = right - left - 1
            area = height * width
            result = max(result, area)

        return result