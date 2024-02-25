# -*- coding = utf-8 -*-
# @Time : 12/21/2023 7:42 PM
# @Author : Lauren
# @File : 438.py
# @Software : PyCharm
from collections import Counter

def findAnagrams(s: str, p: str) -> list[int]:
    res = []
    if len(s) < len(p):
        return res
    left = right = have = 0
    need_map = Counter(p)
    window = {}
    need = len(need_map)
    while right < len(s):
        char = s[right]
        if char in p:
            window[char] = window.get(char, 0) + 1
            if window[char] == need_map[char]:
                have += 1
        right += 1

        while have == need:
            if right - left == len(p):
                res.append(left)
            if s[left] in p:
                window[s[left]] -= 1
                if window[s[left]] < need_map[s[left]]:
                    have -= 1
            left += 1
    return res


def main():
    s1 = "cbaebabacd"
    p1 = "abc"
    s2 = "abab"
    p2 = "ab"
    print(findAnagrams(s1, p1))
    print(findAnagrams(s2, p2))

if __name__ == "__main__":
    main()


