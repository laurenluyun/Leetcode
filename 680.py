# -*- coding = utf-8 -*-
# @Time : 5/29/2023 3:16 PM
# @Author : Lauren
# @File : 680.py
# @Software : PyCharm
'''
easy
114ms, 16.8mb
    1. use reversed string
    2. at most one time, means when the if statement is not met, the return statement can
    decide the result
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        leftIndex = 0
        rightIndex = len(s) - 1
        while leftIndex <= rightIndex:
            if s[leftIndex] != s[rightIndex]:
                string1 = s[:leftIndex] + s[leftIndex + 1:]
                string2 = s[:rightIndex] + s[rightIndex + 1:]
                return string1 == string1[::-1] or string2 == string2[::-1]
            leftIndex += 1
            rightIndex -= 1
        return True

def main():
    mySolution = Solution()
    s1 = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymd" \
         "jgpfdhooxfuupuculmgmqfvnbgtapekouga"
    s2 = "abca"
    s3 = "abc"
    s4 = "enbbe"
    print(mySolution.validPalindrome(s1))
    print(mySolution.validPalindrome(s2))
    print(mySolution.validPalindrome(s3))
    print(mySolution.validPalindrome(s4))

if __name__ == "__main__":
    main()




