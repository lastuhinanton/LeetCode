s1 = "III"
s2 = "LVIII"
s3 = "MCMXCIV"

class Solution:
    mydict = {
        "I":1, "V":5, "X":10,
        "L":50, "C":100, "D":500,
        "M":1000
    }
    def romanToInt(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return self.mydict[s[0]]
        part = self.mydict
        if part[s[0]] < part[s[1]]: return part[s[1]] - part[s[0]] + self.romanToInt(s[2:])
        else: return part[s[0]] + self.romanToInt(s[1:])

element = Solution()
print(element.romanToInt(s1))
print(element.romanToInt(s2))
print(element.romanToInt(s3))