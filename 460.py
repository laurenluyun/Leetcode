# -*- coding = utf-8 -*-
# @Time : 12/29/2023 9:34 PM
# @Author : Lauren
# @File : 460.py
# @Software : PyCharm

class LFUCache():
    # construct cache with specific capacity
    def __init__(self, capacity):
        # key-value pair, KV map
        self.keyToVal = {}
        # key-freq pair, KF map
        self.keyToFreq = {}
        # fre-key pair, FK map
        self.freqToKeys = {}
        # record the minimum frequency
        self.minFreq = 0
        # record the maximum capacity of LFU
        self.cap = capacity

    # search key in the cache, if key exists, return the value, otherwise
    # return -1
    def get(self, key):
        if key not in self.keyToVal:
            return -1
        # increment the freq of key
        self.__increaseFreq(key)
        return self.keyToVal[key]

    # put the key and val into cache, if key exists, modify its val,
    # otherwise if reaches the cap, delete LFU node; insert the (key, val)
    def put(self, key, val):
        if self.cap <= 0:
            return

        # if key already exists, modify the val
        if key in self.keyToVal:
            self.keyToVal[key] = val
            # increment the frequency of key
            self.__increaseFreq(key)
            return

        #if key does not exist, need to insert
        #if reaches the capacity, delete the LFU key
        if self.cap <= len(self.keyToVal):
            self.__removeMinFreqKey()

        # insert key and val, with respective freq = 1
        # insert the KV map
        self.keyToVal[key] = val
        # insert the KF map
        self.keyToFreq[key] = 1
        # insert the FK map
        self.freqToKeys.setdefault(1, set())
        self.freqToKeys[1].add(key)
        # after inserting the new key, the minimum freq is 1
        self.minFreq = 1

    def __increaseFreq(self, key):
        freq = self.keyToFreq[key]
        # updates KF map
        self.keyToFreq[key] = freq + 1
        # update the FK map
        # delete key from the freq list
        self.freqToKeys[freq].remove(key)
        # put the key to the freq + 1 list
        self.freqToKeys.setdefault(freq + 1, set())
        self.freqToKeys[freq + 1].add(key)
        # if the respective list of freq is empty, remove the freq
        if not self.freqToKeys[freq]:
            del self.freqToKeys[freq]
            # if the freq happens to be minFreq, update minFreq
            if freq == self.minFreq:
                self.minFreq += 1

    def __removeMinFreqKey(self):
        # the lisf of key which has the smallest freq
        keyList = self.freqToKeys[self.minFreq]
        # the first key that has been inserted should be deleted
        deletedKey = keyList.pop()
        # update the FK map
        if not keyList:
            del self.freqToKeys[self.minFreq]
        # update the KV map
        del self.keyToVal[deletedKey]
        # update the KF map
        del self.keyToFreq[deletedKey]


