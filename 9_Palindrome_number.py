class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x[::-1] == x

element = Solution()
print(element.isPalindrome(121))
