# s = "hello"
# cmp = "holle"
s = "leetcode"
cmp = "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        my_list = set(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'))
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            while s[left] not in my_list and left < right: left += 1
            while s[right] not in my_list and left < right: right -= 1
            if s[left] in my_list and \
               s[right] in my_list:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)


element = Solution()
if element.reverseVowels(s) != cmp: print("ERROR")
else: print("SUCCESS")
