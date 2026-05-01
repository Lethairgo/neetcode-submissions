class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        window = {}
        countT = {}
        result = [-1, -1]
        minLen = float('inf')

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        left = 0
        have, need = 0, len(countT)

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)
            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    result = [left, right]
                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = result
        return s[left : right + 1] if minLen != float("inf") else ""
            




        
        