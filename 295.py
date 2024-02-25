# -*- coding = utf-8 -*-
# @Time : 7/20/2023 12:42 PM
# @Author : Lauren
# @File : 295.py Find Median from Data Stream
# @Software : PyCharm
import heapq
class MedianFinder:

    def __init__(self):
        self.list = []

    def addNum(self, num: int) -> None:
        self.list.append(num)

    def findMedian(self) -> float:
        self.list.sort()
        if len(self.list) % 2 == 0:
            median = (self.list[len(self.list) // 2 - 1] + self.list[len(
                self.list) // 2]) / 2
        else:
            median = self.list[len(self.list) // 2]
        return median

'''
another solution using Heap data structure: a small heap and a large heap
all elements are all smaller than all elements of the large heap
keep balance of the two heaps, with approximately the same amount of elements
deleting / adding an element to the heap always is an O(logn) operation
finding the max in Max heap is O(1)
finding the min in Min Heap is O(1)
So we will use a Max Heap for the small heap, to get the max value
and a Min Heap for the large Heap, to get the min value

for each insertion, have to follow tw0 rules:
1. all the elements of the small heap should be smaller than all the 
elements of the larger heap
2. the amount of small heap always approximately equals to the amount of 
larger heap, gap to the large is 1
to follow the operation, the time complexity is O(logn)
to find the median is O(1) which is the time complexity of finding the max 
number of small heap, and finding the min of the large heap
538ms, 38.98mb
'''
class MedianFinder01:

    def __init__(self):
        '''
        two heaps: large, small, minheap, maxheap
        heaps should be equal size
        '''
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # push num to the small heap, which is a maxheap
        # python only implements a maxheap, so we have to put -1 in maxheap
        heapq.heappush(self.small, -1 * num)
        # make sure every element in small heap is <= every element in large
        # small and large are non-null, and get the first element of small
        # which is the largest element <= the first element of large which
        # is the first element
        if (self.small and self.large and (-1 * self.small[0]) >
                                           self.large[0]):
            # pop from small heap and then add to large heap
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # if the size of the two heaps are not even
        if len(self.small) > len(self.large) + 1:
            # pop from small heap and then add to large heap
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            # pop from large heap and then add to small heap
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2

def main():
    medianFinder = MedianFinder()
    medianFinder.addNum(3)
    medianFinder.addNum(5)
    print(medianFinder.findMedian())
    medianFinder.addNum(2)
    print(medianFinder.findMedian())

if __name__ == "__main__":
    main()





