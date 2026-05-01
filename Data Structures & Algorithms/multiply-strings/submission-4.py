class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        m, n = len(num1), len(num2)

        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

                d1 = i + j
                d2 = i + j + 1

                total = product + result[d2]
                result[d2] = total % 10
                result[d1] += total // 10

        temp = []
        for digit in result:
            if not (len(temp) == 0 and digit == 0):
                temp.append(str(digit))
        return "".join(temp)