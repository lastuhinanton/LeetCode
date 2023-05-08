pallindrome = "cbbd"

def longestPalindrome(s) -> str:
    longest = [0, 0]
    size_s = len(s)
    for i in range(size_s):
        j = size_s-1
        while i < j:
            tmp = s[i:j+1]
            if tmp[::-1] == tmp:
                if (longest[1] - longest[0]) < (j - i):
                    longest[0], longest[1] = i, j
                j = -1
            j -= 1
    return s[longest[0]:longest[1]+1]

print(longestPalindrome(pallindrome))
