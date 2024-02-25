# -*- coding = utf-8 -*-
# @Time : 4/26/2023 8:00 PM
# @Author : Lauren
# @File : 412.py
# @Software : PyCharm

class Solution_0:
    def fizzBuzz(self, n: int) -> list[str]:
        i = 1
        new_list = []
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                new_list.append("FizzBuzz")
            elif i % 3 == 0:
                new_list.append("Fizz")
            elif i % 5 == 0:
                new_list.append("Buzz")
            else:
                new_list.append(str(i))
            i += 1
        return new_list

class Solution_1:
    def fizzBuzz(self, n: int) -> list[str]:
        new_list = []
        # change to for loop
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                new_list.append("FizzBuzz")
            elif i % 3 == 0:
                new_list.append("Fizz")
            elif i % 5 == 0:
                new_list.append("Buzz")
            else:
                new_list.append(str(i))
        return new_list

class Solution_2:
    # concatenate solution
    def fizzBuzz(self, n: int) -> list[str]:
        new_list = []
        for i in range(1, n + 1):
            element = ''
            if i % 3 == 0:
                element += "Fizz"
            if i % 5 == 0:
                element += "Buzz"
            if element == '':
                element = str(i)
            new_list.append(element)
        return new_list

def main():
    input_1 = 5
    input_2 = 8
    input_3 = 15
    my_solution = Solution_2()
    print(my_solution.fizzBuzz(input_1))
    print(my_solution.fizzBuzz(input_2))
    print(my_solution.fizzBuzz(input_3))

if __name__ == "__main__":
    main()