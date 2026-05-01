class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        visited = set()
        def helper(row, col):
            for r in range(ROWS):
                if matrix[r][col] != 0:
                    matrix[r][col] = 0
                    visited.add((r, col))
            for c in range(COLS):
                if matrix[row][c] != 0:
                    matrix[row][c] = 0
                    visited.add((row, c))

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0 and (r, c) not in visited:
                    helper(r,c)

        
        