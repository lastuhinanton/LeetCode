pallindrome = "cbbd"

def check_pallindrome(start, end, string):
    while start < end:
        if string[start] != string[end]: return False
        start += 1
        end -= 1
    return True

def check_longest(prime, i, j):
    if (prime[1] - prime[0]) < (j - i):
        prime[0], prime[1] = i, j

def longestPalindrome(s) -> str:
    longest = [0, 0]
    for i in range(len(s)):
        j = len(s)-1
        while i < j:
            if check_pallindrome(i, j, s):
                check_longest(longest, i, j)
                j = -1
            j -= 1
    return s[longest[0]:longest[1]+1]

print(longestPalindrome(pallindrome))
