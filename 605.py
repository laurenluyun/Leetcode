# -*- coding = utf-8 -*-
# @Time : 5/18/2023 4:25 PM
# @Author : Lauren
# @File : 605.py
# @Software : PyCharm

'''
Can place flowers
171ms  16.7mb
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        length = len(flowerbed)
        count, prev = 0, 0
        flowerbed.append(0)
        for i in range(0, length):
            if prev == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                count += 1
                flowerbed[i] = 1
            prev = flowerbed[i]
        return n <= count

def main():
    my_solution = Solution()
    list1 = [1,0,0,0,1]
    n1 = 1
    list2 = [0,0,1,0,0]
    n2 = 2
    print(my_solution.canPlaceFlowers(list1,n1))
    print(my_solution.canPlaceFlowers(list2,n2))

if __name__ == "__main__":
    main()
