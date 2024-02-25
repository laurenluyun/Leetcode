# -*- coding = utf-8 -*-
# @Time : 7/21/2023 1:34 PM
# @Author : Lauren
# @File : 424.py Longest Repeating Character Replacement
# @Software : PyCharm
'''
O(26n) => O(n)
we will use a hashmap to count the occurrence of each character
take the character with the highest frequency, and window length - count(
character of the highest frequency) would be the number of elements to be
replaced, which should be <= k => the current window is valid

alternative way to know the occurrence of the most frequent element: keep
the maxf unchanged if we shrink the window, but increase it when we expand
the window, because we only want the maxlength of the valid str => O(n)

when the str is valid, keep expanding the window, with r + 1
when the str is not valid, keep shrinking the window by l - 1 until the str in
valid
178ms, 30.51%, 16.37mb, 79.69%
'''
def characterReplacement(s: str, k: int) -> int:
    count = {}
    res = 0
    l = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res
# slight optimization
def characterReplacement01(s: str, k: int) -> int:
    count = {}
    res = 0
    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res

def characterReplacement02(s: str, k: int) -> int:
    left = res = 0
    if len(s) == 1:
        return 1
    right = 1
    while right < len(s):
        replacement = 0
        while right < len(s):
            if s[right] != s[left] and replacement < k:
                replacement += 1
                right += 1
            elif s[right] == s[left]:
                right += 1
            else:
                break
        res = max(res, (right - left))
        left += 1
        right = left + 1
    return res

def main():
    s1 = "ABAB"
    k1 = 2
    s2 = "AABABBA"
    k2 = 1
    print(characterReplacement02(s1, k1))
    print(characterReplacement02(s2, k2))

if __name__ == "__main__":
    main()
