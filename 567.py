# -*- coding = utf-8 -*-
# @Time : 8/1/2023 4:28 PM
# @Author : Lauren Permutation in String
# extra explanation for Permutation排列组合: same chars in the same size,
# does not care about the order
'''
use hashmap, or array, and sliding window in this case as well, O(n)
58ms, 98.97%, 16.64mb,60.60%
'''
# @File : 567.py
# @Software : PyCharm
from collections import Counter

def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2): return False
    # can use hashmap, but since there's an order in the 26 letters,
    # we can use list, index as the char, 0 => a, value as the occurence of
    # the char 【every letter has its own position in the array】
    s1_arr, s2_arr = [0] * 26, [0] * 26
    # initialize the array for s1, and the sliding window for s2
    for i in range(len(s1)):
        s1_arr[ord(s1[i]) - ord('a')] += 1
        s2_arr[ord(s2[i]) - ord('a')] += 1
    # count the match for the s1_arr and initialized s2-arr
    match = 0
    for j in range(26):
        match += (1 if s1_arr[j] == s2_arr[j] else 0)

    # two pointers to slide the window if the match is not 26, return true
    # if the match is 26
    l = 0
    # slide the window starting from the index of len(s1)
    for r in range(len(s1), len(s2)):
        if match == 26:
            return True
        # find the index of the right pointer
        index = ord(s2[r]) - ord('a')
        # either equals the right pointer
        s2_arr[index] += 1
        if s1_arr[index] == s2_arr[index]:
            match += 1
        # or does not need the right pointer
        elif s1_arr[index] + 1 == s2_arr[index]:
            match -= 1

        # move the left pointer to the right at the same time
        # find the index of the left pointer
        index = ord(s2[l]) - ord('a')
        # either equals the left pointer
        s2_arr[index] -= 1
        if s1_arr[index] == s2_arr[index]:
            match += 1
        # or the left pointer is needed but not included in the current window
        elif s1_arr[index] - 1 == s2_arr[index]:
            match -= 1
        l += 1
    return match == 26

def checkInclusion1(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    need_map = Counter(s1)
    window = {}
    left = right = 0
    have = 0
    need = len(need_map)
    while right < len(s2):
        char = s2[right]
        if char in need_map:
            window[char] = window.get(char, 0) + 1
            if window[char] == need_map[char]:
                have += 1
        right += 1
        print("have, need", have, need)
        print("right, left, right - left", right, left, right - left)
        print(s2[left: right])
        while have == need:
            if right - left == len(s1):
                return True
            if s2[left] in need_map:
                window[s2[left]] -= 1
                if window[s2[left]] < need_map[s2[left]]:
                    have -= 1
            left += 1
    return False


def main():
    s1 = "trinitrophenylmethylnitramine"
    s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"
    s3 = "abcdxabcde"
    s4 = "abcdeabcdx"
    print(checkInclusion1(s1, s2))
    # print(checkInclusion1(s3, s4))

if __name__ == "__main__":
    main()



