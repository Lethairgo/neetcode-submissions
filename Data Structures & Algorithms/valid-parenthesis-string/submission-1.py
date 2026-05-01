class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 1 and s[0] != '*':
            return False

        low, high = 0, 0

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:
                high += 1
                low -= 1

            if high < 0:
                return False
            low = max(0, low)
        return low == 0

