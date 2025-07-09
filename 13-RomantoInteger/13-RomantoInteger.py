# Last updated: 7/8/2025, 9:25:52 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        n = len(s)
        res = 0

        for i in range(n-1):
            if roman_dict[s[i+1]] > roman_dict[s[i]]:
                res -= roman_dict[s[i]]
            else:
                res += roman_dict[s[i]]
        res += roman_dict[s[n-1]]

        return res
