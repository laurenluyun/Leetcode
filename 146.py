# -*- coding = utf-8 -*-
# @Time : 12/28/2023 11:59 PM
# @Author : Lauren
# @File : 146.py
# @Software : PyCharm

# construct node
class Node():
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None

# construct Double Linked List
class DoubleLinkedList():
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # head -> tail
        self.head.next = self.tail
        # head <- tail
        self.tail.prev = self.head
        self.size = 0

    # O(1)
    def addLast(self, x):
        #1 tail.prev <- x
        x.prev = self.tail.prev
        #2 x -> tail
        x.next = self.tail
        #1 tail.prev -> x
        self.tail.prev.next = x
        #2 x -> tail
        self.tail.prev = x
        self.size += 1

    # O(1) remove x
    def remove(self, x):
        # x.prev -> x.next
        x.prev.next = x.next
        # x.prev <- x.next
        x.next.prev = x.prev
        self.size -= 1

    # remove the first node
    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first

    def size(self):
        return self.size

# construct Hashlinkedlist
class LRUCache():
    def __init__(self, capacity):
        self.cap = capacity
        self.map = {}
        self.cache = DoubleLinkedList()
    # need to maintain both DoubleLinkedList and Hashmap at the same time
    # solution: provide an abstract API above these 2 data structures,
    # in order to avoid operating directly on map and cache
    # mark specific key as recently used
    def makeRecently(self, key):
        x = self.map[key]
        # delete the node from the linkedList
        self.cache.remove(x)
        # move the node to the end of the list
        self.cache.addLast(x)

    # add the recently used element
    def addRecently(self, key, val):
        x = Node(key, val)
        # add the node in the linkedList
        self.cache.addLast(x)
        # add the key-value pair in the hashmap
        self.map[key] = x

    def deleteKey(self, key):
        x = self.map[key]
        # remove from the doubledLinkedList
        self.cache.remove(x)
        # remove from the map
        del self.map[key]

    def removeLeastRecently(self):
        # remove the first element (least recently used) from the
        # doubleLinkedList
        deletedNode = self.cache.removeFirst()
        # remove the element through the node, which has both key and value
        del self.map[deletedNode.key]

    def get(self, key):
        if key not in self.map:
            return -1
        # make the node as recently used
        self.makeRecently(key)
        # return the node value
        return self.map[key].val

    def put(self, key, value):
        # if key already exists, modify the val of key and move as recently
        # used
        if key in self.map:
            # delete the node
            self.deleteKey(key)
        # if key does not exist, and reaches the capacity
        elif len(self.map) >= self.cap:
            # delete the leastrecently node
            self.removeLeastRecently()
        # add the new node as recently added node
        self.addRecently(key, value)


