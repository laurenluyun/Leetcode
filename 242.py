# -*- coding = utf-8 -*-
# @Time : 7/11/2023 11:30 PM
# @Author : Lauren
# @File : 242.py
# @Software : PyCharm

from collections import Counter
# Valid anagram success 56ms
def isAnagram(s: str, t: str) -> bool:
    # below is one of the solutions, O(n*2) or O(nlogn), space O(1)
    #return sorted(s) == sorted(t)
    # 65ms, 16.8mb
    return Counter(s) == Counter(t)

# solution hashmap: 70ms, 16.8mb
def isAnagram01(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0) # 0 is the default value
        countT[t[i]] = 1 + countT.get(t[i], 0) # 0 is the default value
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True

def isAnagram01(s: str, t: str) -> bool:
    # 60ms, 17.12mb
    # sortedS = ''.join(sorted(s))
    # sortedT = ''.join(sorted(t))
    # return sortedS == sortedT
    # 65ms, 17.53mb
    charListS = list(s)
    charListS.sort()
    charListT = list(t)
    charListT.sort()
    return charListS == charListT


def main():
    s = "anagram"
    t = "nagaram"
    print(isAnagram01(s, t))


if __name__ == "__main__":
    main()
