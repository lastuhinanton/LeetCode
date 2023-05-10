class Solution:
    def reverse(self, x: int) -> int:
        minus = x < 0
        degree = 2**31
        if x == -degree: return 0

        x = str(x)
        if minus: x = x[1:]
        number = int(x[::-1])

        if number < -degree or \
            number > (degree - 1):
            return 0
            
        if minus: return -number
        return number



number = Solution()
print(number.reverse(int(input())))