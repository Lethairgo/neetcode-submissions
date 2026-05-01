class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        i, j = 0, len(heights) - 1

        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            maximum = max(maximum, area)
            if heights[i] < heights[j]:
                i += 1
            else: 
                j -= 1
        
        return maximum