# -*- coding = utf-8 -*-
# @Time : 5/30/2023 6:56 PM
# @Author : Lauren
# @File : 524.py
# @Software : PyCharm

'''
Longest Word in Dictionary through Deleting
133ms 18.8mb
'''

class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        ans = ""
        for word in dictionary:
        # the iter() function is used to create an iterator object from an
        # iterable, combined with for loop and next()
            ss = iter(s)
            if all(c in ss for c in word) and (
                    len(word) > len(ans) or len(word) == len(
                    ans) and word < ans):
                ans = word
        return ans


def main():
    mySolution = Solution()
    s1 = "abpcplea"
    dictionary1 = ["ale","apple","monkey","plea"]

    s2 = "abpcplea"
    dictionary2 = ["a","b","c"]

    print(mySolution.findLongestWord(s1, dictionary1))
    print(mySolution.findLongestWord(s2, dictionary2))

if __name__ == "__main__":
    main()

