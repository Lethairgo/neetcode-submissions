class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * COLS for _ in range(ROWS)]

        self.prefix_sum[0][0] = matrix[0][0]
        for i in range(1, ROWS):
            self.prefix_sum[i][0] = self.prefix_sum[i - 1][0] + matrix[i][0]

        for j in range(1, COLS):
            self.prefix_sum[0][j] = self.prefix_sum[0][j - 1] + matrix[0][j]

        for i in range(1, ROWS): 
            for j in range(1, COLS):
                self.prefix_sum[i][j] = (
                    matrix[i][j] +
                    self.prefix_sum[i - 1][j] +
                    self.prefix_sum[i][j - 1] -
                    self.prefix_sum[i - 1][j - 1]
                )
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prefix_sum[row2][col2]
        if row1 > 0:
            result -= self.prefix_sum[row1 - 1][col2]
        if col1 > 0:
            result -= self.prefix_sum[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            result += self.prefix_sum[row1 - 1][col1 - 1]
        return result


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)