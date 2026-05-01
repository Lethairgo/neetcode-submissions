class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n

        while True:
            # moving slow
            temp = 0
            while slow > 0:
                digit = slow % 10
                temp += digit ** 2
                slow //= 10
            slow = temp

            # moving fast
            temp = 0
            while fast > 0:
                digit = fast % 10
                temp += digit ** 2
                fast //= 10
            fast = temp

            # moving fast
            temp = 0
            while fast > 0:
                digit = fast % 10
                temp += digit ** 2
                fast //= 10
            fast = temp

            if fast == 1:
                return True
            elif fast == slow:
                return False