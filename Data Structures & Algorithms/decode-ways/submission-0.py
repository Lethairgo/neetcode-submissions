class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        prev1, prev2 = 1, 1

        for i in range(2, len(s) + 1):
            temp = 0
            if s[i - 1] != '0':
                temp += prev1
            
            if 10 <= int(s[i - 2 : i]) <= 26:
                temp += prev2

            prev1, prev2 = temp, prev1
        
        return prev1
        