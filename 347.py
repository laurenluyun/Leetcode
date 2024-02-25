# -*- coding = utf-8 -*-
# @Time : 7/13/2023 10:15 AM
# @Author : Lauren
# @File : 347.py  Top K frequent elements
# @Software : PyCharm

'''
Bucket Sort, key is the element itself, value is the number of occurrence
but in this case, we have unlimited range of the value of the key, which is the
element of the list could range to infinite
so, instead of having the occurrence as the value, we put the occurrence as the
key (bounded to the length of the list)
and respective element which has the exact number of occurrence in a list
as the value
to scan for the top k occurring values - look from the end of the hashmap
O(n)  132ms, 22MB
'''
def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    for n in nums:
        # get the current count of n in hashmap n, increment by 1, if n is
        # new , then give the default value 0
        count[n] = 1 + count.get(n, 0)
    # it will return the key-value pair added to the hashmap
    for n, c in count.items():
        # count as the index ranges from 0-length(the nested list be in
        # the ascending order), n is the element of each list
        freq[c].append(n)

    res = []
    # traverse the nested list in descending order
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res

def topKFrequent01(nums: list[int], k: int) -> list[int]:
    count = {}
    frequency = [[] for i in range(len(nums) + 1)]
    for each in nums:
        count[each] = count.get(each, 0) + 1
    # iterate over the key-value pairs, key is the number, value is the
    # occurrence, now reverse the key and the value and convert to a nested
    # list, which is in a non-descending order in terms of occurrence
    for n, c in count.items():
        frequency[c].append(n)
    res = []
    for i in range(len(frequency) - 1, 0, -1):
        for n in frequency[i]:
            res.append(n)
            if len(res) == k:
                return res
'''
frequency = [[] for i in range(len(nums) + 1)]:
This creates a list of empty lists. Specifically, it creates a list with 
len(nums) + 1 empty lists. Each inner list is a separate object in memory, 
and they are distinct from each other. You can append elements to each inner 
list without affecting the others. This is commonly used to create a 
list of lists for various purposes, such as storing data in a tabular format.

frequency = [[] * len(nums)]:
This creates a list containing len(nums) references to the same empty list 
object. In other words, all the inner lists are the same list object in 
memory. Any modification to one of these inner lists will affect all of them, 
as they are essentially aliases to the same list. This behavior is likely not 
what you want when storing frequencies because it will lead to incorrect 
results.

'''




def main():
    nums1 = [1,1,1,2,2,3]
    k1 = 2
    nums2 = [1]
    k2 = 1
    print(topKFrequent01(nums1, k1))
    print(topKFrequent01(nums2, k2))

if __name__ == "__main__":
    main()
