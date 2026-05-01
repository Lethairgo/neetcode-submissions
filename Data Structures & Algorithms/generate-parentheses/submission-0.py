class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtracking(left, right):
            if left == right == n:
                result.append("".join(stack))
                return

            if left < n:
                stack.append('(')
                backtracking(left + 1, right)
                stack.pop()
            if right < left:
                stack.append(')')
                backtracking(left, right + 1)
                stack.pop()

        backtracking(0, 0)
        return result