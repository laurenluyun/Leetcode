# -*- coding = utf-8 -*-
# @Time : 7/17/2023 8:50 AM
# @Author : Lauren
# @File : 125.py Valid Palindrome
# @Software : PyCharm

# 59ms 76.91, 17.94mb
def isPalindrome(s: str) -> bool:
    non_alnum_chars = [char.lower() for char in s if char.isalnum()]
    if len(non_alnum_chars) <= 1:
        return True
    for index in range(len(non_alnum_chars) // 2):
        if non_alnum_chars[index] != non_alnum_chars[len(non_alnum_chars) - 1 - index]:
            return False
    return True
# 64ms 57.02%, 17.01, 68.74
def isPalindrome2(s: str) -> bool:
    newStr = "" #efficient, but extra memory
    for c in s:
        if c.isalnum(): # built-in function
            newStr += c.lower()
    return newStr[::-1] == newStr

def alphNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))
# 101ms, 5.4%, 17.24, 39.23%
def isPalindrome3(s: str) -> bool:
    # less efficient, but no extra memory, no built-in function
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alphNum(s[l]):
            l += 1
        while r > l and not alphNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True








def main():
    s1 = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    s3 = " "
    print(isPalindrome(s1))
    print(isPalindrome(s2))
    print(isPalindrome(s3))

if __name__ == "__main__":
    main()