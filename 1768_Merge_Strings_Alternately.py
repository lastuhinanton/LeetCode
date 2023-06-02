word1 = "abcd"
word2 = "pq"

class Solution:
    def mergeAlternately(self, word1, word2):
        if not word1: return word2
        elif not word2: return word1
        else:
            return word1[0] + word2[0] + self.mergeAlternately(word1[1:], word2[1:])

element = Solution()
print(element.mergeAlternately(word1, word2))