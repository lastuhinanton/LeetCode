strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0]

        # for i in strs[1:]:
        #     idx = 0
        #     len_sample = len(strs[0])
        #     len_element = len(i)
        #     while len_element > idx and len_sample > idx and strs[0][idx] == i[idx]: idx += 1
        #     strs[0] = strs[0][:idx]
        # return strs[0]


element = Solution()
print(element.longestCommonPrefix(strs1))
print(element.longestCommonPrefix(strs2))
