# -*- coding = utf-8 -*-
# @Time : 5/27/2023 9:17 PM
# @Author : Lauren
# @File : 76.py
# @Software : PyCharm

'''
from Neetcode
minimum window substring(hard) - sliding window
134ms, 17mb
'''
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # cases where nothing will be returned
        if not s or not t or len(s) < len(t):
            return ''
        # Counter()
        # return a dict where key is the element in t, value is the
        # occurrence of each element.
        # the count value will be returned for existing elements,
        # and 0 will be returned for elements that have not occurred in the
        # iterable
        countT = Counter(t)
        window = {}

        # number of required chars we have, and number of required
        # chars we need
        have, need = 0, len(countT)

        # initialize result: a list of the left index and right index
        # result length is initialized to the largest possible floating-point value
        result, resultLen = [-1, -1], float("infinity")
        leftIndex = 0

        # right index is moving to the right every iteration
        for rightIndex in range(len(s)):
            char = s[rightIndex]
            # restore the right char in the window and update the occurence
            # by 1, get the value of the char, the default value is 0
            window[char] = 1 + window.get(char, 0)

            # if the char is needed and the number of this char in the
            # current window equals to the number needed, add the number of
            # have(elements required) by 1
            if char in countT and window[char] == countT[char]:
                have += 1

            # when the number of characters needed = number of characters
            # required
            while have == need:
                # update our result, when the length of the current window
                # is less than the previous result Length
                if (rightIndex - leftIndex + 1) < resultLen:
                    result = [leftIndex, rightIndex]
                    resultLen = rightIndex - leftIndex + 1
                # then pop from the left of the current window, by deduct
                # the occurence of the left char in the window, and update
                # the leftIndex, to minimize the window
                window[s[leftIndex]] -= 1
                # if the removed left char is needed and also make the
                # number of the current char less than the number required
                if s[leftIndex] in countT and window[s[leftIndex]] < \
                        countT[s[leftIndex]]:
                    have -= 1
                leftIndex += 1

        leftIndex, rightIndex = result
        # the if statement makes sure the program returns "" when there is
        # no match between s and t
        return s[leftIndex : rightIndex + 1] if resultLen != float(
            "infinity") else ""


def minWindow(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""
    # initialize 2 hashmaps
    need_map = Counter(t)
    window = {}
    # initialize 2 counters
    need = len(need_map)
    start = have = 0
    # initialize 2 pointers
    left = right = 0
    res_length = float("infinity")
    # move the right pointer
    while right < len(s):
        char = s[right]
        if char in need_map:
            window[char] = 1 + window.get(char, 0)
            # only when the values equal can we say we have the char added
            # in the window
            if window[char] == need_map[char]:
                have += 1
        right += 1
        print("have, need", have, need)
        print("left, right", left, right)
        print(s[left : right])
        while have == need:
            if right - left < res_length:
                start = left
                res_length = right - left
            if s[left] in need_map:
                window[s[left]] -= 1
                if window[s[left]] < need_map[s[left]]:
                    have -= 1
            left += 1
            print("start, res_length", start, res_length)
    return s[start: start + res_length] if res_length != float("infinity") \
        else ""

def main():
    s = "aba"
    t = "aa"
    print(minWindow(s, t))

if __name__ == "__main__":
    main()




