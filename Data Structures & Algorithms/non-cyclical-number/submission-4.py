class Solution:
    def isHappy(self, n: int) -> bool:
        def calculateNext(n):
            temp = 0
            while n > 0:
                digit = n % 10
                temp += digit ** 2
                n //= 10
            return temp

        slow, fast = n, n

        while True:
            # moving slow
            slow = calculateNext(slow)

            # moving fast
            fast = calculateNext(calculateNext(fast))

            if fast == 1:
                return True
            elif fast == slow:
                return False