class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        # row search
        midRow = 0
        while top <= bottom:
            midRow = (top + bottom) // 2
            if matrix[midRow][0] == target:
                return True
            elif matrix[midRow][0] < target:
                top = midRow + 1
            else:
                bottom = midRow - 1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[bottom][mid] == target:
                return True
            elif matrix[bottom][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False