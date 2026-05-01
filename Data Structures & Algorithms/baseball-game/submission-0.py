class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == '+':
                temp = stack[-1] + stack[-2]
                stack.append(temp)
            elif operation == 'D':
                temp = stack[-1] * 2
                stack.append(temp)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)