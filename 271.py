# -*- coding = utf-8 -*-
# @Time : 7/15/2023 10:10 AM
# @Author : Lauren
# @File : 271.py Encode and Decode Strings
'''
Design an algo to encode a list of strings to a string. The encoded string is
then sent over the network and is decodes back to the original lit of strings
0(n)
'''
# @Software : PyCharm
class Solution:
    '''
    parameter: strs - a list of strings
    return: encodes a list of strings to a single string
    '''
    def encode(self, strs):
        res = ""
        for each in strs:
            res += str(len(each)) + "#" + each
        return res

    '''
    parameter: str - a string
    return: decodes a single string to a list of strings
    '''
    def decode(self, str):
        # use pointer to know what is the index we are at
        res, i = [], 0
        while i < len(str):
            j = i
            while str[j] != "#":
                j+= 1
            # get the length of current string
            length = int(str[i:j])
            res.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return res


def main():
    mySolution = Solution()
    strs1 = ["lint", "code", "love", "you"]
    strs2 = ["we", "say", ":", "yes"]
    print(mySolution.encode(strs1))
    print(mySolution.encode(strs2))
    print(mySolution.decode(mySolution.encode(strs1)))
    print(mySolution.decode(mySolution.encode(strs2)))

if __name__ == "__main__":
    main()
