s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "1"
s5 = ""
s6 = "dvdf"

def lengthOfLongestSubstring(s):
    longest = 0
    tmp = []
    for i in s:
        if i in tmp:
            if len(tmp) > longest: longest = len(tmp)
            while i in tmp:
                tmp = tmp[1:]
        tmp.append(i)
    if len(tmp) > longest: longest = len(tmp)
    return longest

print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))
print(lengthOfLongestSubstring(s4))
print(lengthOfLongestSubstring(s5))
print(lengthOfLongestSubstring(s6))

