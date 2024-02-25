# -*- coding = utf-8 -*-
# @Time : 7/12/2023 9:44 AM
# @Author : Lauren
# @File : 49.py
# @Software : PyCharm
from collections import defaultdict
'''
defaultdict(list) is a specialized dictionary object from the collections 
module that automatically creates a new list as the default value for 
any non-existent key. It provides a convenient way to handle cases where you 
want to associate multiple values with a key without explicitly initializing 
the list for each key.
'''

# group anagrams
# if use sorted the time complexity will be m * nlog(n), m is the number of
# elements in the list, n is the length of each element
# if we use hashmap, the time complexity will be O(m * n) 131ms,
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list) # mapping charCount to list of Anagrams
    for s in strs:
        count = [0] * 26 # a, b ,....z, denoted by 0, 1, 2, 3...
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s) # key is the count, which denotes the
        # number of occurence of each character, which can specify the anagram
    return res.values()

def groupAnagrams01(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    # we can iterate over an empty string
    for str in strs:
        count = [0] * 26
        for char in str:
            count[ord(char) - ord('a')] += 1
        # res[count].append(str), lists are mutable, cannot be used as keys,
        # need to convert to tuples
        res[tuple(count)].append(str)
    return res.values()


def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    strs1 = [""]
    strs2 = ["a"]
    print(groupAnagrams01(strs))
    print(groupAnagrams01(strs1))
    print(groupAnagrams01(strs2))

if __name__ == "__main__":
    main()
