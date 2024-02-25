# -*- coding = utf-8 -*-
# @Time : 7/21/2023 9:48 AM
# @Author : Lauren
# @File : 3.py Longest Substring Without Repeating Characters
# @Software : PyCharm

# def lengthOfLongestSubstring(s: str) -> int:
#     l, r, maxlen = 0, 1, 1
#     if len(s) == 0:
#         return 0
#     substring = s[0:l]
#     while r < len(s):
#         if s[r]
#         while s[r] not in substring:
#             substring = s[l:r]
#             r += 1
#         maxlen = max(r - l, maxlen)
#         l = r
#         r += 1
#     return maxlen

'''
time and memory complexity = O(n) 74ms, 71.44%, 16.37ms, 82.39%
use set for substring to avoid duplicates
'''
def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = res = 0
    for r in range(len(s)):
        # while there's duplicate, keep removing the left most element until
        # there is no duplicate in the set
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        # if there is no duplicate, add the new element to the set and
        # calculate the length
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

def main():
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    print(lengthOfLongestSubstring(s1))
    print(lengthOfLongestSubstring(s2))
    print(lengthOfLongestSubstring(s3))


if __name__ == "__main__":
    main()
