# -*- coding = utf-8 -*-
# @Time : 5/8/2023 1:06 PM
# @Author : Lauren
# @File : 13.py
# @Software : PyCharm

class Solution:
    # 49ms 16.3mb
    def romanToInt(self, s: str) -> int:
        dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                      "M": 1000}
        number = 0
        # roman subtract only applies to I, X, C, and can only be
        # added before the number which is 10 times or 5 times of them:
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += dictionary[char]
        return number

    # 63 ms, 16.2MB
    def romanToInt_1(self, s: str) -> int:
        dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                      "M": 1000}
        sum = dictionary[s[len(s) - 1]]
        for i in range(len(s) - 1):
            if dictionary[s[i]] < dictionary[s[i + 1]]:
                sum -= dictionary[s[i]]
            else:
                sum += dictionary[s[i]]
        return sum

def main():
    roman_1 = 'III'
    roman_2 = 'LVIII'
    roman_3 = 'MCMXCIV'

    my_solution = Solution()
    print(my_solution.romanToInt(roman_1))
    print(my_solution.romanToInt(roman_2))
    print(my_solution.romanToInt(roman_3))

if __name__ == "__main__":
    main()
