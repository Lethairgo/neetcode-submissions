class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while True:
            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)
                temp = 0
                while n > 0:
                    digit = n % 10
                    temp += digit ** 2
                    n //= 10
                n = temp
