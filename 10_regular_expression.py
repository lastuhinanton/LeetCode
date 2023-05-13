

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    # def __init__(self):s
    #     self.si = 0
    #     self.pi = 0
    #     self.result = True

    # def isMatch(self, s: str, p: str) -> bool:
    #     if self.pi < len(p):
    #         if p[self.pi] == '.': self.pi, self.si = self.pi+1, self.si+1
    #         elif p[self.pi] == '*':
    #             if self.pi+1 != len(p):
    #                 if p[self.pi+1] in s[self.si+1:]:
    #                     self.si = s[self.si:].index(p[self.pi+1])+self.si
    #                     self.pi += 1
    #                 else:
    #                     self.result = False
    #                     return self.result
    #             else:
    #                 self.result = True
    #                 self.si = len(s)
    #                 return self.result
    #         else:
    #             if s[self.si] == p[self.pi]: self.pi, self.si = self.pi+1, self.si+1
    #             else:
    #                 self.result = False
    #                 return self.result
    #         return self.isMatch(s, p)

    #     if self.pi == len(p):
    #         if self.si == len(s):
    #             self.result = True
    #             return self.result
    #         else:
    #             self.result = False
    #             return self.result

element = Solution()
print(element.isMatch("aaaaaaaaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*"))