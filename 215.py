# -*- coding = utf-8 -*-
# @Time : 1/15/2024 8:02 PM
# @Author : Lauren
# @File : 215.py
# @Software : PyCharm
import heapq


class Solution:
    # below heap is more efficient
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # 小顶堆，堆顶是最小元素
        pq = []
        for each in nums:
            # 每一个元素都要过一遍二叉堆
            heapq.heappush(pq, each)
            # 堆中元素数量>k时，删除堆顶元素
            if len(pq) > k:
                heapq.heappop(pq)
        # pq中剩下的是num中K个最大元素，堆顶是最小的，即第K个最大的元素
        return pq[0]

class Solution1:
    # time limit exceeded
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def partition(nums, lo, hi):
            pivot = nums[hi]
            i = lo - 1
            # compare ech element in the nums with pivot
            for j in range(lo, hi):
                if nums[j] >= pivot:
                    i += 1
                    # swap i and j
                    nums[i], nums[j] = nums[j], nums[i]
            #  It ensures that the pivot element (which is initially at
            #  nums[high]) is moved to the correct position in the array
            #  after the partitioning. The pivot is now at the index i + 1,
            #  and all elements to the left of it are greater than or equal
            #  to the pivot, while all elements to the right are smaller.
            nums[i + 1], nums[hi] = nums[hi], nums[i + 1]
            return i + 1

        def quicksort(nums, lo, hi, k):
            if lo <= hi:
                partition_index = partition(nums, lo, hi)
                if partition_index == k:
                    return nums[partition_index]
                # 太大了 往右找
                elif partition_index < k:
                    return quicksort(nums, partition_index + 1, hi, k)
                else:
                    return quicksort(nums, lo, partition_index - 1, k)
        return quicksort(nums, 0, len(nums) - 1, k - 1)


