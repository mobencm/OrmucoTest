from DoublyLinkedList import *
from datetime import datetime
import time

class LRUCache:
    def __init__(self, cacheSize,ttl = None):
        self.cacheSize = cacheSize
        self.item_list = DoublyLinkedList(cacheSize)
        self.pageMap = {}
        self.ttl = ttl

    def accessPage(self, data):
        pageNode = None
        if (data in self.pageMap):
            # If page is present in the cache, move the existing item to the head of item_list
            pageNode = self.pageMap.get(data);
            self.item_list.movePageToHead(pageNode);
        else:
            # If the page is not present in the cache, append it to the front of item_list
            if (self.item_list.getCurrSize() == self.item_list.getSize()):
                # Remove the last item if the length of cache exceeds the upper bound.
                del self.pageMap[self.item_list.getTail().getdata()]

            pageNode = self.item_list.addPageToList(data)
            self.pageMap[data] = pageNode

    def DeleteExpired(self):
        now = datetime.now()
        for item in self.item_list:
            time_delta = now - item.timestamp
            if time_delta.seconds > self.ttl:
                del self.pageMap[item.getdata()]
                self.item_list.remove_current()

cacheSize = 4
cache =  LRUCache(cacheSize,ttl=1)
cache.accessPage(3)
cache.accessPage(4)
cache.accessPage(6)

cache.accessPage(7)
cache.accessPage(8)
cache.accessPage(7)
cache.accessPage(17)
for key in cache.pageMap :
    print(key)
print ( 20 *'#')
cache.accessPage(6)
cache.accessPage(17)
cache.accessPage(18)


for key in cache.pageMap :
    print(key)
print ( 20 *'#')
time.sleep(3)
cache.accessPage(9)
cache.DeleteExpired()

for key in cache.pageMap :
    print(key)