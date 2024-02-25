# -*- coding = utf-8 -*-
# @Time : 5/21/2023 3:55 PM
# @Author : Lauren
# @File : 763.py
# @Software : PyCharm
'''
Partition Labels  Greedy Algo
在处理数组前，统计一遍信息（如频率、个数、第一次出现位置、最后一次出现位置等）可
以使题目难度大幅降低。
'''

class Solution:
    # 47ms, 16.5MB
    def partitionLabels(self, s: str) -> list[int]:
        dict= {}
        for index in range(len(s)):
            if s[index] not in dict.keys():
                dict[s[index]] = []
                dict[s[index]].append(index)
            else:
                dict[s[index]].append(index)

        output = []
        start, max_end = 0, 0
        for value in dict.values():
            if value[0] <= max_end:
                max_end = max(max_end, max(value))

            else:
                length = max_end - start + 1
                output.append(length)

                start = value[0]
                max_end = max(value)

        output.append(len(s) - sum(output))
        return output

class Solution1:
    # 54ms, 16.2MB
    def partitionLabels(self, s: str) -> list[int]:
        # the dictionary lastIndex keeps track of the last occurrence of each character
        lastIndex = {}
        res = []
        '''
        The enumerate() function in Python is used to iterate over a sequence 
        (such as a list, tuple, or string) while keeping track of the index 
        position of each element. It returns an iterator that yields pairs 
        of the form (index, element).
        '''
        for index, char in enumerate(s):
            lastIndex[char] = index
        '''
        {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21}
        {'e': 8, 'c': 9, 'b': 6, 'd': 7}
        '''
        size, end = 0, 0
        for index, char in enumerate(s):
            size += 1
            end = max(end, lastIndex[char])
            if index == end:
                res.append(size)
                size = 0
        return res


def main():
    my_solution = Solution1()
    s1 = "ababcbacadefegdehijhklij"
    s2 = "eccbbbbdec"
    print(my_solution.partitionLabels(s1))
    print(my_solution.partitionLabels(s2))

if __name__ == "__main__":
    main()
