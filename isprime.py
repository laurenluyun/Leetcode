# -*- coding = utf-8 -*-
# @Time : 1/21/2024 1:33 AM
# @Author : Lauren
# @File : isprime.py
# @Software : PyCharm

'''
this program includes 3 approaches to decide if a number is a prime number
'''
import math

# time O(sqrt(n)) space O(1)
def is_prime_1(n):
    # if n is not a prime number, it must have at least one factor less than
    # or equal to its square root. If there were a factor greater than the
    # square root, there would also have to be a corresponding factor smaller
    # than the square root to yield the product n.
    # int does not perform ceiling
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# time O(n^2) space O(n)
def is_prime_2(n):
    factors = list(range(2, n))
    # divide n by numbers ranging from 2 to n-1,if cannot exact division
    # then remove the number
    # problem: the factors list is being modified while being iterated
    # for each in factors:
    #     if n % each != 0:
    #         factors.remove(each)

    # Use list comprehension to create a new list without undesired elements
    factors = [each for each in factors if n % each == 0]
    # if the factors is not empty, there's number in the factor that can be
    # exactly divided, hence n is not a prime number
    if factors:
        return False
    # else return True
    return True

# time O(n) space O(1)
def is_prime_3(n):
    for i in range(2, n):
        if i != 1 and i != n and n % i == 0:
            return False
    return True


# Example usage
def main():
    num_1 = 1 #T
    num_2 = 2 #T
    num_3 = 3 #T
    num_4 = 4 #F
    num_5 = 5 #T
    num_6 = 6 #F
    num_7 = 7 #T
    # print("=======1=======")
    # print(is_prime_1(num_1))
    # print(is_prime_1(num_2))
    # print(is_prime_1(num_3))
    # print(is_prime_1(num_4))
    # print(is_prime_1(num_5))
    # print(is_prime_1(num_6))
    # print(is_prime_1(num_7))
    # print("=======2=======")
    print(is_prime_2(num_1))
    print(is_prime_2(num_2))
    print(is_prime_2(num_3))
    print(is_prime_2(num_4))
    print(is_prime_2(num_5))
    print(is_prime_2(num_6))
    print(is_prime_2(num_7))
    # print("=======3=======")
    # print(is_prime_3(num_1))
    # print(is_prime_3(num_2))
    # print(is_prime_3(num_3))
    # print(is_prime_3(num_4))
    # print(is_prime_3(num_5))
    # print(is_prime_3(num_6))
    # print(is_prime_3(num_7))

if __name__ == "__main__":
    main()

