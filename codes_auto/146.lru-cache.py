#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] lru-cache
#
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.dts=OrderedDict()
        self.capacity=capacity


    def get(self, key: int) -> int:
        if key in self.dts:
            self.dts.move_to_end(key)
            return self.dts[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dts:
            self.dts[key]=value
            self.dts.move_to_end(key)
        else:
            if len(self.dts)==self.capacity:
                self.dts.popitem(0)
            self.dts[key]=value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end