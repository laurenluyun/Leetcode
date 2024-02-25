# -*- coding = utf-8 -*-
# @Time : 12/23/2023 6:42 PM
# @Author : Lauren
# @File : 659.py
# @Software : PyCharm


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])

            res.append(str[(j + 1) : (j + 1 + length)])
            i = j + 1 + length
        return res

def main():
    mySolution = Solution()
    list1 = ["lint", "code", "love", "you"]

    list2 = ["we", "say", ":", "yes"]

    print(mySolution.decode(mySolution.encode(list1)))
    print(mySolution.decode(mySolution.encode(list2)))
    # print(mySolution.encode(list1))
    # print(mySolution.decode("4#lint4#code4#love3#you"))

if __name__ == "__main__":
    main()
