class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if stack and pairs[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            
        