class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for c in s:
            if c in mapping.values():  # opening bracket
                stack.append(c)
            elif c in mapping:  # closing bracket
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()
            else:
                return False  # invalid character (optional)
                
        return len(stack) == 0