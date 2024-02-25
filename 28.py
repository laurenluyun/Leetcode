# -*- coding = utf-8 -*-
# @Time : 5/13/2023 10:46 AM
# @Author : Lauren
# @File : 28.py
# @Software : PyCharm

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # string.find(substring) return the index of the substring, and -1
        # if it is not found
        return haystack.find(needle)
        # similar function except for ValueError if it is not found
        # return haystack.index(needle)
def main():
    needle = "leeto"
    haystack = "leetcode"
    mySolution = Solution()
    print(mySolution.strStr(haystack, needle))

if __name__ == "__main__":
    main()
