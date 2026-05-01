class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0

        while x:
            digit = x % 10
            x //= 10

            if result > MAX // 10 or (result == MAX // 10 and digit > 7):
                return 0
            result = result * 10 + digit
        return result * sign