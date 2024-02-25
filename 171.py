# -*- coding = utf-8 -*-
# @Time : 11/9/2023 11:17 AM
# @Author : Lauren
# @File : 171.py
# @Software : PyCharm

# 37ms 16.18mb
def titleToNumber(columnTitle: str) -> int:
    res = 0
    reversed_columnTitle = columnTitle[::-1]
    for index, char in enumerate(reversed_columnTitle):
        res += (26 ** index) * (ord(char) - 64)
    return res



def main():
    columnTitle1 = "A"
    columnTitle2 = "AB"
    columnTitle3 = "ZY"

    print(titleToNumber(columnTitle1))
    print(titleToNumber(columnTitle2))
    print(titleToNumber(columnTitle3))

if __name__ == "__main__":
    main()
