test_string = "0000000000012345"

class Solution:
	def myAtoi(self, s: str) -> int:
		index = 0
		minus = 0
		sign = True
		number = list()
		s = s.strip()
		if index == len(s): return 0
		if s[index] == '-' or s[index] == '+':
			if s[index] == '-': minus += 1
			index += 1
		if index == len(s): return 0
		if not s[index].isnumeric(): return 0
		if minus % 2 == 1: sign = False
		while s[index].isnumeric():
			number.append(s[index])
			index += 1
			if index == len(s): break
		number = int(''.join(number))
		if not sign: number = -number
		if number > 2**31 - 1: number = 2**31 - 1
		elif number < -2**31: number = -2**31
		return number

obj = Solution()
print(obj.myAtoi(test_string))
