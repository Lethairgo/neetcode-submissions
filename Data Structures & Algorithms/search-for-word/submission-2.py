class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        def dfs(row, col, i):
            if i == len(word):
                return True

            if (min(row, col) < 0) or row >= rows or col >= cols or word[i] != board[row][col] or board[row][col] == '#':
                return False
            
            board[row][col] = '#'

            result = dfs(row + 1, col, i + 1) or dfs(row - 1, col, i + 1) or dfs(row, col + 1, i + 1) or dfs(row, col - 1, i + 1)
            board[row][col] = word[i]
            return result

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False


        