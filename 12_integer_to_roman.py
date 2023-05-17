class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        numbers = {
            1:"I", 4:"IV", 5:"V", 9:"IX",
            10:"X", 40:"XL", 50:"L", 90:"XC",
            100:"C", 400:"CD", 500:"D", 900:"CM",
            1000:"M"
        }
        keys = sorted(numbers.keys())[::-1]
        for i in keys:
            if num // i > 0:
                result += numbers[i] * (num // i)
                num %= i
        return result


element = Solution()
print(element.intToRoman(1001))
