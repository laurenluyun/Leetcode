# -*- coding = utf-8 -*-
# @Time : 5/9/2023 12:10 PM
# @Author : Lauren
# @File : 14.py
# @Software : PyCharm

'''
Write a function to find the longest common prefix
string amongst an array of strings.
If there is no common prefix, return an empty string "".
49ms 16.5mb

Takeway:
If the array is sorted alphabetically then you can assume that the first
element of the array and the last element of the array will have most
different prefixes of all comparisons that could be made between strings
in the array. If this is true, you only have to compare these two strings.
'''


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = ""
        # Sorting a list of strings will return a new list of strings with
        # the original elements arranged in lexicographically ascending order
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans




def main():
    lst_1 = ["flower","flow","flight"]
    lst_2 = ["dog","racecar","car"]
    my_solution = Solution()
    print(my_solution.longestCommonPrefix(lst_1))
    print(my_solution.longestCommonPrefix(lst_2))

if __name__ == "__main__":
    main()