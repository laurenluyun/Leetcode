# -*- coding = utf-8 -*-
# @Time : 12/30/2023 1:53 PM
# @Author : Lauren
# @File : 4602nd.py
# @Software : PyCharm
import collections


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        # val - doubleLinkedList pair
        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)
        self.map[val] = node
        self.right.prev = node
        node.prev.next = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            next, prev = node.next, node.prev
            next.prev = prev
            prev.next = next
            self.map.pop(val, None)

    def popLeft(self):
        res = self.left.next.val
        self.pop(self.left.next.val)
        return res

    def update(self, val):
        self.pop(val)
        self.pushRight(val)

class LFUCache:
    def __init__(self, capacity):
        self.cap = capacity
        # least frequently used count
        self.lfuCnt = 0
        self.valMap = {} # key -value pair map
        self.countMap = collections.defaultdict(int) # key -> count map
        # count -> linkedList map
        self.listMap = collections.defaultdict(LinkedList)

    def counter(self, key):
        # update the key->count map
        cnt = self.countMap[key]
        self.countMap[key] += 1
        # update the count -> linkedList map
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)

        # if the original cnt is the lfu and the listmap is now empty,
        # we have to update the lfu to be lfucnt + 1
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

    def get(self, key):
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]


    def put(self, key, value):
        if self.cap == 0:
            return

        # if the key is a new key and we've reached the capacity, we need to
        if key not in self.valMap and len(self.valMap) == self.cap:
            # pop out the lfu and the leftmost(oldest) node
            res = self.listMap[self.lfuCnt].popLeft()
            self.valMap.pop(res)
            self.countMap.pop(res)
        # then we add the key value
        self.valMap[key] = value
        # update the both countmap and listmap in the counter()
        self.counter(key)
        # update the lfucnt when the count of the current key is < current
        # lfucnt
        self.lfuCnt = min(self.lfuCnt, self.countMap[key])

