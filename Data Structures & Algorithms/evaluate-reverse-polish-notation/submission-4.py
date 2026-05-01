class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = []

        for i in range(len(tokens)):
            char = tokens[i]
            if char == '+' or char == '-' or char == '*' or char == '/':
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())

                match char:
                    case '+':
                        result = operand1 + operand2
                    case '-':
                        result = operand1 - operand2
                    case '*':
                        result = operand1 * operand2
                    case '/':
                        result = int(operand1 / operand2)
                stack.append(result)
            else:
                stack.append(char)
        return stack[0]



        