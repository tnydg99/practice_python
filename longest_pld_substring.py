def longestPalindrome(s):
    longest_palindrome = ''
    if len(s) == 0:
        return ''
    s1 = s[0:int(len(s)/2)]
    s2 = s[int(len(s)/2):len(s)]
    extra_letter = '' if len(s1) == len(s2) else s2[0]
    if extra_letter != '':
        s2 = s2[1:]
    for i in range(len(s1)):
        if s1[len(s1)-i-1] == s2[i]:
            extra_letter = s1[len(s1)-i-1] + extra_letter + s2[i]
    # for i in range(len(s)):
    #     substring = s[i:len(s)]
    #     if substring == substring[::-1] and len(substring) > len(longest_palindrome):
    #         longest_palindrome = substring
    if longest_palindrome == '':
        longest_palindrome = s[0]
    return longest_palindrome


if __name__ == "__main__":
    print(longestPalindrome('cabal'))