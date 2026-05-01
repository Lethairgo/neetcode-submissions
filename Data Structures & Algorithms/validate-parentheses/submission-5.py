class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in map:
                stack.append(c)
            else:
                if stack and map[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            
        