string = "PAYPALISHIRING"

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        prime = dict()
        pos = 0
        down = True
        for i in s:
            if pos not in prime: prime[pos] = list()
            prime[pos].append(i)
            if down: pos += 1
            else: pos -= 1
            if pos == 0: down = True
            elif pos == numRows-1: down = False
        result = str()
        for i in sorted(prime.keys()):
            result += "".join(prime[i])
        return result

tmp = Solution()
print(tmp.convert(string, 3))